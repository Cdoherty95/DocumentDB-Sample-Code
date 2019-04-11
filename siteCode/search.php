<?php
/**
 * https://www.youtube.com/watch?v=IBofrKP1Aa4
 * http://makble.com/mongodb-find-query-examples-with-php
 */

// Requiring the AWS SDK
require 'vendor/autoload.php';


# Global variables to store information about the DocumentDB Cluster
$DatabaseUserName = '';
$DatabasePassword = '';
$DatabaseEndpoint = '';


$mongodbURI = "mongodb://$DatabaseUserName:$DatabasePassword@$DatabaseEndpoint:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0";
// Instanciate MongoDB client class
$client = new MongoDB\Client($mongodbURI);
// Variable selecting the customer_information_db database
$customerInformationDB = $client->customer_information_db;
// Variable selecting the collection
$customerCollection = $customerInformationDB->customers;

if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $query = $_POST['firstName'];
}

$documentlist = $customerCollection->find(
    ['firstName' => $query]
);

foreach ($documentlist as $customer)
{
    var_dump($customer);
}

?>