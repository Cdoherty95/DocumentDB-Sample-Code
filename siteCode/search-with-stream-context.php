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

$SSL_DIR = "/home/ubuntu";
$SSL_FILE = "rds-combined-ca-bundle.pem";

$ctx = stream_context_create(
    array(
        "ssl" => array(
            /* Certificate Authority the remote server certificate must be signed by */
            "cafile"            => $SSL_DIR . "/" . $SSL_FILE,

            /* Disable self signed certificates */
            "allow_self_signed" => false,

            /* Verify the peer certificate against our provided Certificate Authority root certificate */
            "verify_peer"       => true, /* Default to false pre PHP 5.6 */

            /* Verify the peer name (e.g. hostname validation) */
            /* Will use the hostname used to connec to the node */
            "verify_peer_name"  => true,

            /* Verify the server certificate has not expired */
            "verify_expiry"     => true, /* Only available in the MongoDB PHP Driver */
        ),
    )
);

$client = new MongoClient(
    "mongodb://$DatabaseUserName:$DatabasePassword@$DatabaseEndpoint:27017",
    array("ssl" => true),
    array("context" => $ctx)
);


//$mongodbURI = "mongodb://$DatabaseUserName:$DatabasePassword@$DatabaseEndpoint:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0";
// Instantiate MongoDB client class
//$client = new MongoDB\Client($mongodbURI);
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