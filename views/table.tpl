
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
  <title></title>

  <style type="text/css">
    * { margin: 0; padding: 0; }

    body {
      font-family: Verdana, sans-serif;
      font-size: 14px;
      /* ie6 hack */
      height: 100%;
      overflow: auto;
    }
	
	    
      font-family: Verdana, sans-serif;
      font-size: 14px;
      /* ie6 hack */
      height: 100%;
      overflow: auto;
    }

    p { margin: 20px; }

    #footer_bar {
      width: 100%;

      position: fixed;
      top: 0;
      overflow: hidden;
    }
       #bar_container {
         background: #FAA53A;
         margin: 0 auto;
         width: 900px;
         height: 35px;
         overflow: hidden;
       }
           #bar_container ul {
             list-style: none;
           }
               #bar_container ul li {
                 float: left;
                 width: 150px;
                 text-align: center;
               }
                  #bar_container ul li a {
                    color: white;
                    display: block;
                    font-weight: bold;
                    padding: 10px 0;
                    text-decoration: none;
                    width: 150px;
                  }
                      #bar_container ul li a:hover {
                        background-color: #F68529;
                      }



    /* IE6 hack */
    * html #footer_bar {
      position: absolute;
    }


  </style>


</head>



<body>

<p style="background-color:green; color:white; font-size: 20px;  height: 35px;"><b>Bentornato !!!</b></p>

<div id="footer_bar">
  <div id="bar_container">
    <ul>
      <li><a href="http://192.168.0.60:8080/home">Home</a></li>
      <li><a href="http://192.168.0.60:8080/tabella">Tabella</a></li>
      <li><a href="http://192.168.0.60:8080/about">About</a></li>
      <li><a href="http://192.168.0.60:8080/refresh">Aggiorna DB</a></li>
      <li><a href="http://192.168.0.60:8080/delete">Svuota DB</a></li>
      <li><a href="http://192.168.0.60:8080/login">Logout</a></li>
    </ul>
  </div>
</div>

<table style="margin: 100px auto; border: 2px solid black; width: 900px;">
    <tr>
    <th align="center">DATA</th><th align="center">TEMPERATURA C°</th>
    </tr>
    % for riga in righe:
    <tr >
    <td align="center">{{riga[0]}}</td>
    <td align="center">{{riga[1]}}</td>
    </tr>
    % end
    </table>
	
	

</body>
	




</html>
