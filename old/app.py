from flask import Flask
app= Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi Página</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    </head>
    <body class="bg-gray-100">
        <div class="container mx-auto mt-10">
            <div class="max-w-sm mx-auto bg-white rounded-lg overflow-hidden shadow-lg">
                <div class="carousel rounded-t-lg">
                    <img src="https://scontent.fmex10-5.fna.fbcdn.net/v/t39.30808-6/399657436_996389291464735_4183128353583945664_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeFLs_WfOlKed0sQBS3HTH0Sq2VW4Esuj7mrZVbgSy6PuXgf5z_W1qdu6AqbrqFrHMfybCzNdoVPJMezJ9VVhRaG&_nc_ohc=07Ps0bhrWC0Q7kNvgGP2cfF&_nc_zt=23&_nc_ht=scontent.fmex10-5.fna&oh=00_AYBWiFhGHkLSN0URYeDwkBSHDrsWKwBz0nsctgLQVGSmsw&oe=6666A61D" alt="image 1" class="h-60 w-full object-cover">
                </div>
                <div class="p-5">
                    <div class="mb-3 flex items-center justify-between">
                        <h5 class="text-xl font-medium text-blue-gray-700">Adolfo Angel Hdez Manuel</h5>
                        <div class="flex items-center gap-1.5 text-yellow-700">
                            <i class="material-icons">person</i>
                            <span>9 "A"</span>
                        </div>
                    </div>
                    <p class="text-gray-700">Web desplegada en render utilizando python con flask, haciendo uso de git con gitHub.</p>
                </div>
                    <div class="p-5 flex justify-end space-x-2">
                        <button class="material-icons text-blue-500"><a href='https://web.facebook.com'>facebook</a></button>
                         <button class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" onclick="mostrarMensaje()">Dar clic</button>
                    </div>
            </div>
        </div>
        <script>
             function mostrarMensaje() {
                Swal.fire({
                    title: '¡Gracias por ver!',
                    text: 'Bonito día :)',
                    icon: 'success',
                    confirmButtonText: 'Cerrar'
                });
            }
        </script>
        <script src="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.js"></script>
    </body>
    </html>
    '''

if __name__=='__main__':
    app.run(debug=True)