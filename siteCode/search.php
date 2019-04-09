<?php
/**
 * https://www.youtube.com/watch?v=IBofrKP1Aa4
 * http://makble.com/mongodb-find-query-examples-with-php
 */

// Requiring the AWS SDK
require 'vendor/autoload.php';

// Instanciate MongoDB client class
$client = new MongoDB\Client;
// Variable selecting the customer_information_db database
$customerInformationDB = $client->customer_information_db;
// Variable selecting the collection
//$collection = $customerInformationDB->collectionName;

if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $query = $_POST['firstName'];
}

$documentlist = $customerInformationDB->find(
    ['firstName' => $query]
);

foreach ($documentlist as $customer)
{
    var_dump($customer);
}

?>