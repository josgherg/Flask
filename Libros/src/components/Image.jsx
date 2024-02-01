function Image(){

    return(
        <section className="imagenPreview">
             <div className="parte1Preview">
                <h1 className="tipo1 blanco">¡Bienvenido!</h1>
                <br/>
                <h2 className="tipo2 blanco">Dejanos llevarte al interesante mundo de los Libros. </h2>
                <br />
                <h1 className="tipo3 blanco">¡Ven y encuentra el tuyo!</h1>
            </div>
            <div className="parte2Preview">
                <div className="divImagen"> 
                     <img id="img1" src="./src/assets/preview.jpg" alt="" />
                </div>
            </div>
        </section>
    );
}

export default Image;