const express = require('express');
const path = require('path');
const dotenv = require('dotenv');
const { authMiddleware } = require('./utils/validateToken');

dotenv.config({ path: path.resolve(__dirname, '.env') });

const app = express();
const port = Number(process.env.PORT || 4010);

app.use(express.json());

const products = [
  { id: 1, name: 'Laptop Pro 14', price: 1299.99, category: 'Hardware' },
  { id: 2, name: 'Monitor 27" 4K', price: 799.99, category: 'Hardware' },
  { id: 3, name: 'Teclado mecánico', price: 149.99, category: 'Periféricos' },
  { id: 4, name: 'Auriculares inalámbricos', price: 199.99, category: 'Audio' },
];

app.get('/health', (req, res) => {
  res.json({
    ok: true,
    status: 'healthy',
    service: 'lab-azuread-oauth2-pkce-api',
    timestamp: new Date().toISOString(),
    port,
  });
});

app.get('/api/products', authMiddleware, (req, res) => {
  res.json({
    ok: true,
    message: 'Acceso autorizado mediante OAuth2 PKCE + Azure AD.',
    user: {
      oid: req.user.oid,
      preferred_username: req.user.preferred_username,
      name: req.user.name,
      aud: req.user.aud,
      iss: req.user.iss,
    },
    products,
  });
});

app.use((req, res) => {
  res.status(404).json({
    ok: false,
    message: 'Endpoint no encontrado.',
    path: req.originalUrl,
  });
});

app.use((err, req, res, next) => {
  console.error('Error no manejado:', err);
  res.status(500).json({
    ok: false,
    message: 'Error interno del servidor.',
    error: err.message,
  });
});

app.listen(port, () => {
  console.log(`API local ejecutándose en http://localhost:${port}`);
  console.log(`Health check: http://localhost:${port}/health`);
  console.log(`Endpoint protegido: http://localhost:${port}/api/products`);
  console.log(`Azure JWKS: ${process.env.AZURE_JWKS_URI || 'No configurado'}`);
});
