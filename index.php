<?PHP
// mysql server
 	$dbserver = 'localhost';
	$dbuser = 'root';
	$dbpass = '';
	$dbname ='test';
	
	$imgName = strval(time()).'.jpg';
	$target_dir = 'uploads/';
	
	$data = file_get_contents('php://input');
	if (!(file_put_contents($target_dir . $imgName,$data) === FALSE)) {
		$con = mysqli_connect($dbserver,$dbuser,$dbpass,$dbname);
		$sql = "INSERT INTO tbl_img VALUES ('$imgName')";
		mysqli_query($con,$sql) or die(mysqli_error(). "<hr/>Line: ". __LINE__ ."<br/>$sql");
		
		mysqli_close($con);
		echo 'OK';
		
	}else echo 'failed';

?>