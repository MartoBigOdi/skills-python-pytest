# XPATH tips para armar segun se necesiten
# text
# //label[text()='Full name* ']

# contains
# //label[contains(text(),'Partial value')]

# index
# label[x]   x es el index que queremos ubicar cuando tenemos por ejemplo 22 img.

# or & AND --> utilizamos dos expresiones para bsucar el elemento o una o la otra o una y la otra
# //input[@type='number' or //*[@id="content"]/div/div/div/input]
# //input[@type='number' and //*[@id="content"]/div/div/div/input]

# Buscamos segun arbol del dom
"""
<div id="content" class="large-12 columns">
        <div class="example">
  <h2>Login Page</h2> ------> ESTE ES EL ELEMENTO QUE BUSCAMOS
  <h4 class="subheader">This is where you can log into the secure area. Enter <em>tomsmith</em> for the username and <em>SuperSecretPassword!</em> for the password. If the information is wrong you should see error messages.</h4>
  <form name="login" id="login" action="/authenticate" method="post">
     <div class="row">
      <div class="large-6 small-12 columns">
        <label for="username">Username</label>
        <input type="text" name="username" id="username"> ----> INPUT DEL MISMO FRAGMENTO 
      </div>
    </div>
    <div class="row">
      <div class="large-6 small-12 columns">
        <label for="password">Password</label>
        <input type="password" name="password" id="password">
      </div>
    </div>
      <button class="radius" type="submit"><i class="fa fa-2x fa-sign-in"> Login</i></button>
  </form>
</div>
"""
# //div[@id='content']/child::div/child::h2  ------> ESTE ES EL ELEMENTO QUE BUSCAMOS

# following-sibling
# //label[text()='Username']//following::input -----> INPUT DEL MISMO FRAGMENTO













