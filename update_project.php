<?php
    include('connection.php');
    $con = connection();

    $id = $_GET['proj_id'];

    $sql = "SELECT * FROM projects WHERE `proj_id` = '$id'";
    $query = mysqli_query($con, $sql);
    $row = mysqli_fetch_array($query);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Edit project</title>
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="./assets/css/tailwind.output.css" />
    <script
      src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js"
      defer
    ></script>
    <script src="./assets/js/init-alpine.js"></script>
</head>
<body>
        <form action="edit_project.php" method="POST">
              <div
                class="px-4 py-3 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800"
              >
                <input
                    type="hidden"
                    name="id"
                    value="<?= $row['proj_id'] ?>"
                />
                <label class="block text-sm">
                  <span class="text-gray-700 dark:text-gray-400">Name:</span>
                  <input
                    type="text"
                    name="name"
                    required
                    class="block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input"
                    value="<?= $row['proj_name'] ?>"
                    />
                </label>
                <br>

                <label class="block text-sm">
                  <span class="text-gray-700 dark:text-gray-400">Description:</span>
                  <textarea 
                    name="description" 
                    class="block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-textarea focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray" 
                    rows="3"
                    placeholder="<?= $row['proj_description'] ?>"
                  >
                  </textarea>
                </label>
                <br>

                <label class="block text-sm">
                  <span class="text-gray-700 dark:text-gray-400">Due date:</span>
                  <input
                    type="date"
                    name="dueDate"
                    required
                    class="block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input"
                    value="<?= $row['proj_due_date'] ?>"
                    />
                </label>
                <br>

                <div>
                  <input
                    type="submit" 
                    class="px-4 py-2 text-sm font-medium leading-5 text-white transition-colors duration-150 bg-purple-600 border border-transparent rounded-lg active:bg-purple-600 hover:bg-purple-700 focus:outline-none focus:shadow-outline-purple"
                    value="Save changes"
                    >
                </div>
                <br>
            </form>
</body>
</html>