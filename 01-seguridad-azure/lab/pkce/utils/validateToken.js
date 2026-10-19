const jwt = require('jsonwebtoken');
const jwksClient = require('jwks-rsa');

const jwks = jwksClient({
  jwksUri: process.env.AZURE_JWKS_URI || 'https://login.microsoftonline.com/common/discovery/v2.0/keys',
  cache: true,
  cacheMaxEntries: 5,
  rateLimit: true,
  jwksRequestsPerMinute: 10,
});

function getExpectedIssuers() {
  const issuers = (process.env.VALID_ISSUERS || process.env.AZURE_ISSUER || '').split(',').map((issuer) => issuer.trim()).filter(Boolean);
  if (issuers.length === 0) {
    issuers.push(process.env.AZURE_ISSUER || 'https://login.microsoftonline.com/common/v2.0');
  }
  return issuers;
}

function getExpectedAudiences() {
  const audienceValues = [
    process.env.API_AUDIENCE,
    process.env.AZURE_API_CLIENT_ID,
    `api://${process.env.AZURE_API_CLIENT_ID || ''}`,
    process.env.AZURE_CLIENT_ID,
  ].filter(Boolean);

  return audienceValues.length > 0 ? audienceValues : ['api://default'];
}

function getSigningKey(kid) {
  return new Promise((resolve, reject) => {
    jwks.getSigningKey(kid, (error, key) => {
      if (error) {
        reject(error);
        return;
      }

      const signingKey = key?.publicKey || key?.rsaPublicKey;
      if (!signingKey) {
        reject(new Error('No se pudo obtener la clave pública del JWKS de Azure AD.'));
        return;
      }

      resolve(signingKey);
    });
  });
}

function decodeTokenWithoutVerification(token) {
  try {
    const decoded = jwt.decode(token, { complete: true });
    return decoded;
  } catch (error) {
    return null;
  }
}

async function validateAccessToken(token) {
  if (!token) {
    throw new Error('Falta el token Bearer en la cabecera Authorization.');
  }

  const cleanToken = token.replace(/^Bearer\s+/i, '').trim();
  if (!cleanToken) {
    throw new Error('El token Bearer está vacío.');
  }

  const decodedHeader = decodeTokenWithoutVerification(cleanToken);
  if (!decodedHeader || !decodedHeader.header || !decodedHeader.header.kid) {
    throw new Error('El JWT no tiene un header válido o no incluye kid.');
  }

  const payload = jwt.decode(cleanToken);
  if (!payload || typeof payload !== 'object') {
    throw new Error('El JWT no tiene payload válido.');
  }

  if (typeof payload.exp !== 'number' && typeof payload.exp !== 'string') {
    throw new Error('El token JWT no incluye el claim exp.');
  }

  if (typeof payload.nbf !== 'number' && typeof payload.nbf !== 'string') {
    throw new Error('El token JWT no incluye el claim nbf.');
  }

  const expectedIssuers = getExpectedIssuers();
  const expectedAudiences = getExpectedAudiences();

  if (payload.aud === undefined || payload.aud === null) {
    throw new Error('El token JWT no incluye el claim aud.');
  }

  const decodedPayload = payload;
  const audienceList = Array.isArray(decodedPayload.aud) ? decodedPayload.aud : [decodedPayload.aud];
  const isAudienceValid = audienceList.some((aud) => expectedAudiences.includes(aud));
  if (!isAudienceValid) {
    throw new Error(`El token JWT no fue emitido para esta API. Audiencias esperadas: ${expectedAudiences.join(', ')}`);
  }

  if (!expectedIssuers.includes(decodedPayload.iss)) {
    throw new Error(`El issuer del token JWT no es válido. Emisor recibido: ${decodedPayload.iss}`);
  }

  const signingKey = await getSigningKey(decodedHeader.header.kid);

  return new Promise((resolve, reject) => {
    jwt.verify(
      cleanToken,
      signingKey,
      {
        algorithms: ['RS256', 'RS384', 'RS512'],
        issuer: expectedIssuers,
        audience: expectedAudiences,
      },
      (error, verifiedToken) => {
        if (error) {
          reject(new Error(`La firma o los claims del JWT no son válidos: ${error.message}`));
          return;
        }

        resolve(verifiedToken);
      }
    );
  });
}

function authMiddleware(req, res, next) {
  const authHeader = req.headers.authorization;

  validateAccessToken(authHeader)
    .then((decoded) => {
      req.user = decoded;
      next();
    })
    .catch((error) => {
      res.status(401).json({
        ok: false,
        message: 'Token no válido o caducado.',
        error: error.message,
      });
    });
}

module.exports = {
  validateAccessToken,
  authMiddleware,
  getExpectedIssuers,
  getExpectedAudiences,
};
