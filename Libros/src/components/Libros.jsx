import { useState, useEffect } from 'react';

function Libros(){
    const [libros, setLibros] = useState(null);
    const[comentarios, setComentarios] = useState();
    const [enlaceApiLibros] = useState('http://127.0.0.1:7500/libreria/ver/info')

    useEffect(()=>{
        const infoApiLibros = async ()=>{
          try{
            const respuesta = await fetch(enlaceApiLibros);
            if(respuesta.ok){
              const datos = await respuesta.json()
              setLibros(datos) 
            }else{
              console.error('error al recibir datos de la Api')
            }
          }catch(error){
            console.log(error)
          }
        }
        infoApiLibros()
    },[enlaceApiLibros])

    useEffect(()=>{
      const infoComentarios = async ()=>{
        let comentarios = []
        let tituloa, titulop, index2 = 0;
         for (let index =0; index<libros.length; index++){
          let item = libros[index];
          tituloa = item.titulo;
          let datosLibros=[]
          let opiniones=[]
          libros.map((item2)=>{
            titulop = item2.titulo;
            if (titulop == tituloa){
              index2 += 1;  
              if (datosLibros.length == 0){
                datosLibros.push(item.id)
                datosLibros.push(item.titulo)
                datosLibros.push(item.nombreAutores)
                datosLibros.push(item.nombreGeneros)
                if (item.nombre !=null){
                  opiniones.push(item2.nombre);
                opiniones.push(item2.contenido);
                }
                datosLibros.push(opiniones)
                opiniones=[]
              }else{
                if (item.nombre !=null){
                  opiniones.push(item2.nombre);
                opiniones.push(item2.contenido);
                }
                datosLibros.push(opiniones)
                opiniones = []
                index=index2+1;
                index2 = 0;
              }
            }
            })
          comentarios.push(datosLibros)
        }  
        setComentarios(comentarios)
     }
    infoComentarios()
  },[libros])
  
  return(
    <>
      {comentarios && comentarios.map((item, index)=>{
    
        return (     
          <>
            <div key={index} className="content5">
                <div className="parte2_1ViewContainer">
                    <h1 className="tipo4 azul">{item[1]  }</h1>
                    <br/>
                    <h3 className="tipo4 azul">{"Por " + item[2]}</h3>
                    <br/>
                    <h3 className="tipo4 azul">{"Género: " + item[3]}</h3>
                </div>
                <div className="parte2_2ViewContainer">
                  <img id="img3" src="./src/assets/how_Linux_Works.jpeg" alt="" />
                </div>
                <div className="parte2_3ViewContainer"> 
                {item.map((itemn, index)=>{ 
                  return(
                    <>
                  {itemn.length!=0 && index > 3?
                        <>
                          <h4 className="tipo4 azul">{itemn[0] + ":"}</h4>  
                          <h4 className="tipo4 azul">{"\""+itemn[1] + "\""}</h4>  
                    </>
                    :itemn.length==0 && index > 3?
                      <>
                        <h4 className="tipo4 azul">No existe ningún comentario actualmente.</h4>   
                    </>:''}
                </>  
                )         
                }
                )}
                </div>
            </div>
          </>
      )
      })
      }
    </>

) 
  
}

export default Libros;

      