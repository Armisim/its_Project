<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<title>Login</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<link rel="stylesheet" href="http://www.italianisticaonline.it/wp-admin/wp-admin.css" type="text/css" />
	<script type="text/javascript">
	function focusit() {
		document.getElementById('log').focus();
	}
	window.onload = focusit;
	</script>
</head>
<body>

<div id="login">


<form name="loginform" id="loginform" action="/login" method="post">
<p><label>Nome utente:<br /><input type="text" name="username" id="log" value="" size="20" tabindex="1" /></label></p>
<p><label>Password:<br /> <input type="password" name="password" id="pwd" value="" size="20" tabindex="2" /></label></p>

<p class="submit">
	<input type="submit" name="submit" id="submit" value="Login &raquo;" tabindex="4" />
	<input type="hidden" name="redirect_to" value="wp-admin/" />
</p>
</form>

</div>

</body>
</html>

  

