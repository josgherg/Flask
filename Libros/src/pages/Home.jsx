import Libros from '../components/Libros';

function Home(){
    return(
        <main className="principal2">
            <section className="viewContainer">
                <div className="parte1ViewContainer">
                    <h1 className="tipo4 negro">Tus Libros</h1>
                    <hr/>
                    <div className="parte1_1ViewContainer">
                        <h1 className="tipo4 blanco titulosparte1_1VC">Título y Autor</h1>
                        <h1 className="tipo4 blanco titulosparte1_1VC">Carátula</h1>
                        <h1 className="tipo4 blanco titulosparte1_1VC">Comentarios</h1>
                    </div>
                </div>
                <div  className="parte2ViewContainer">
                    <Libros/>
                </div>
            </section>
        </main>    
    )
}

export default Home;