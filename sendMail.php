<?
$to = $_GET['to'];
$ip = getenv("REMOTE_ADDR");
mail($to,'IP Change',$ip,'From: ipController');
?> 
