<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

try {
    try {
        throw new Exception("A");
    } finally {
        throw new Exception("B");
    }
} catch(Exception $e){
    var_dump($e);
}

