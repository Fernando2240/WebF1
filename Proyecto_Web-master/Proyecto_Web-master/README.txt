README

Para la ejecución del proyecto se debe hacer lo siguiente:
clona o descarga el proyecto, lo descomprime, una vez descomprimido se abre en visual studio code,
seguido a esto se abre el XAMPP y se le da en start al Apache y al MySQL, luego se le da Admin al MySQL
para hacer la conexión a la base de datos llamada card_mvd que se encuentra en el código en la parte 
del server, src, Data y en el archivo .sql, con el codigo que se encuentra ahí lo que hay que hacer es 
copiar y pegar en PhpMyAdmin en la parte de SQL. Volviendo al visual studio code, en la terminal se 
ejecuta el comando cd client para acceder a ese directorio y luego el comando npm install para instalar 
los modulos de node, estos mismos pasos se hacen para el server. Luego nuevamengte en la terminal escribo 
el comando npm install init vite@latest CARRITO para instalar el directorio .vite que sirve para desarrollar 
un entorno rápido y eficiente. Por último se ejecuta dos terminales consecutivamente donde en uno se pone el 
comando cd client y luego npm run dev, en el otro terminal se pone el comando cd server y seguido a esto 
npm run dev, luego de ejecutados estos comandos en la terminal del client saldrá el siguiente enlace 
Local:   http://localhost:5173/ para ingresar a la página web, se le da ctrl + click sobre él e ingresa a la página.
