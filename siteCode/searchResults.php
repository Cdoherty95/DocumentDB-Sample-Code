<?php
/**
 * https://www.youtube.com/watch?v=IBofrKP1Aa4
 * http://makble.com/mongodb-find-query-examples-with-php
 * https://www.php.net/manual/en/mongo.connecting.ssl.php
 * https://github.com/mongodb/mongo-php-library/issues/361
 */

// Requiring the AWS SDK
require 'vendor/autoload.php';

// Global variables to store information about the DocumentDB Cluster
$DatabaseUserName = '';
$DatabasePassword = '';
$DatabaseEndpoint = '';

// Location of AWS .pem file to create an SSL/TSL encrypted connection
$SSL_DIR = "/home/ubuntu";
$SSL_FILE = "rds-combined-ca-bundle.pem";

// Variable to define where to find the .pem file and the options we want to use to connect
$ctx = stream_context_create(
    array(
        "ssl" => array(
            /* The remote server's public key file provided by AWS */
            "cafile"            => $SSL_DIR . "/" . $SSL_FILE,

            /* Disable self signed certificates */
            "allow_self_signed" => false,

            /* Verify the peer certificate against our provided Certificate Authority root certificate */
            "verify_peer"       => true,

            /* Verify the peer name (e.g. hostname validation) */
            /* Will use the hostname used to connect to the node */
            "verify_peer_name"  => true,

            /* Verify the server certificate has not expired */
            "verify_expiry"     => true,
        ),
    )
);

// Instantiate a new instance of the mongodb client
$client = new MongoDB\Client(
// URI of our documentdb cluster endpoint
    "mongodb://$DatabaseUserName:$DatabasePassword@$DatabaseEndpoint:27017/",
    [
        'username' => $DatabaseUserName,
        'password' => $DatabasePassword,
        'ssl' => true,
    ],
    [
        // referencing the variable above which defines the SSL stream options
        'context' => $ctx,
    ]
);

// Variable telling the client which database we want to use i.e. customer_information_db
$customerInformationDB = $client->customer_information_db;

// Variable telling the client which cluster within the database we want to use i.e. customers
$customerCollection = $customerInformationDB->customers;

// This statement to gets the user's input from the Post method used by the HTML form
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $query = $_POST['firstName'];
}

// Variable to hold the BSON object returned from MongoDB when the search is executed
// This statement uses the MongoDB client object pointing to the desired collection to search for the name
$resultsFromQuery = $customerCollection->find(

// Tells the client which field we want to search and for what value
    ['firstName' => $query]
);

var_dump($resultsFromQuery);

// This loop iterates through the BSON object returned from our query
foreach ($resultsFromQuery as $customer)
{
    echo $customer["birthDate"]["year"];
}

echo '<a href="index.html"><h1>Search Again</h1></a>';

?>