<?PHP


    $value=$_GET['val'];
    
	// mysql server
 	$dbserver = 'localhost';
	$dbuser = 'testuser';
	$dbpass = 'test123';
	$dbname ='testdb';
	
	$con = mysqli_connect($dbserver,$dbuser,$dbpass,$dbname);
	
	$sql = "SELECT COUNT(*) FROM result";
	$result = mysqli_query($con,$sql) or die(mysqli_error(). "<hr/>Line: ". __LINE__ ."<br/>$sql");
	 $rs = mysqli_fetch_array($result);
	 if ($value=='count'){
	 	echo  $rs[0];
	 }
	 mysqli_free_result($result); 
	mysqli_close($con);
	
	
	
	
	
?>