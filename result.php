



<?PHP

    $idval = intval($_GET['id']);
	$value=$_GET['val'];
    
	// mysql server
 	$dbserver = 'localhost';
	$dbuser = 'testuser';
	$dbpass = 'test123';
	$dbname ='testdb';
	
	
	
	$con = mysqli_connect($dbserver,$dbuser,$dbpass,$dbname);
	
	$sql = "select * from result where id=$idval";
	$result = mysqli_query($con,$sql) or die(mysqli_error(). "<hr/>Line: ". __LINE__ ."<br/>$sql");
	 $rs = mysqli_fetch_array($result);
	 if ($value=='imagename'){
	 	echo  $rs[1];
	 }
	 elseif ($value=='username'){
		 echo $rs[2];
	 }
	 elseif ($value=='tweet'){
		 echo $rs[3];
	 }
	 else{
		 echo "invalid";
	 }
	 mysqli_free_result($result); 
	mysqli_close($con);
	//echo $idval;
	//echo $value;
	
?>