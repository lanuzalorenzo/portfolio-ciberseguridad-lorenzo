<?php
declare(strict_types=1);

session_start();

$page = $_GET['page'] ?? __DIR__ . '/pages/home.php';
?>
<!doctype html>
<html lang="es">
<head><meta charset="utf-8"><title>Lab de inclusión de ficheros</title></head>
<body>
<h1>Lab de inclusión de ficheros</h1>
<p>PHP <?= htmlspecialchars(PHP_VERSION, ENT_QUOTES, 'UTF-8') ?></p>
<?php include $page; ?>
</body>
</html>
