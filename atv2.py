<?php
session_start();

$validEmail = "caio@gmail.com";
$validPassword = "123";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST["email"];
    $password = $_POST["password"];

    if (empty($email) || empty($password)) {
        $error_message = "Invalid email or password. Please try again.";
    } else if ($email === $validEmail && $password === $validPassword) {
        $_SESSION["user"] = "Caio";
        header("Location: index.php");
        exit;
    } else {
        $error_message = "Invalid email or password. Please try again.";
    }
}
?>

<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://cdn.tailwindcss.com"></script>
    <title>Login</title>
</head>

<body>
    <div class="flex justify-center items-center w-screen   h-screen">
        <div class="border border-black p-5 shadow-xl w-[300px]">

            <?php if (isset($error_message)): ?>
                <div class="pt-5 pb-5 text-left">
                    <p>
                        <?php echo $error_message; ?>
                    </p>
                </div>

            <?php elseif (isset($_SESSION["user"])): ?>
                <div class="pt-5 pb-5 text-left">
                    <p>
                        Welcome, <?php echo $_SESSION["user"]; ?>
                    </p>
                </div>

            <?php endif; ?>

            <form method="post" action="">
                <div class="flex flex-col gap-2 w-full h-full ">
                    <input id="email" name="email" required class=" p-1 pl-2 pr-2 border border-zinc-400 rounded" placeholder="Email" type="email" />
                    <input name="password" required id="password" class=" p-1 pl-2 pr-2 border border-zinc-400 rounded" placeholder="Senha" type="password" />
                    <button class="p-1 border border-zinc-600 rounded active:bg-gray-500">
                        <h1 class="text-center">Submit</h1>
                    </button>
                    <div class="flex justify-between">
                        <a href="#" class="text-sm">Criar conta</a>
                        <a href="#" class="underline text-sm">Esqueci minha senha</a>
                    </div>
                </div>
            </form>
        </div>
    </div>
</body>

</html>