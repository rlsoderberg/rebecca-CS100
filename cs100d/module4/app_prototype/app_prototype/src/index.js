import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';


//i don't understand how this is working!!! it says File data/db.json not found, so i'm guessing it's not working?
//const [images, setImages] = useState([])
//i tried this and this didn't work either! 
//import imageData from './data/db.json';
//i tried json-loader, with this next line, and webpack.config.json, but that didn't work
//const json = require('json-loader!./data/db.json');

//so all my attempts to load the json from the file aren't working!!! i'm just putting it all in here for now...
//const obj = JSON.parse('{"images":[{"id":1,"filename":"1843.jpg","decade":"1840s","source":"The Metropolitan Museum of Art","info":"Former U.S. president John Quincy Adams - early dagguerotype by Philip Haas.","title":"First Presidential Photograph"},{"id":2,"filename":"1855.jpg","decade":"1850s","source":"Royal Collection Trust","info":"A British colonel, and two Russian boys, apparently taken prisoner, during the Crimean War - photo by Roger Fenton","title":"Crimean War"},{"id":3,"filename":"1862.jpg","decade":"1860s","source":"The Metropolitan Museum of Art","info":"U.S. President Abraham Lincoln visits Antietam Wood after the Civil Wars Battle of Antietam - photo by Alexander Gardner","title":"Civil War"},{"id":4,"filename":"1877.jpg","decade":"1870s","source":"Library of Congress","info":"Thomas Edison and his early phonograph","title":"Thomas Edison invents phonograph"},{"id":5,"filename":"1884.jpg","decade":"1880s","source":"Library of Congress","info":"Workers build the Statue of Liberty inside French sculptor Frederic Auguste Bartholdis workshop - photo by Pierre Petit","title":"Statue of Liberty constructed"},{"id":6,"filename":"1899p2.jpg","decade":"1890s","source":"Wellcome Collection Gallery","info":"Nikola Tesla sitting in his Colorado Springs laboratory next to his Tesla coil - photo by Dickinson V. Alley","title":"Nikola Tesla - Tesla Coil"},{"id":7,"filename":"1902p1.jpg","decade":"1900s","source":"Breve Storia del Cinema","info":"A frame from the French silent fantasy film 'Le Voyage dans La Lune' by Georges Melies","title":"Le Voyage dans La Lune"},{"id":8,"filename":"1903p1.jpg","decade":"1900s","source":"Library of Congress","info":"First successful flight of the Wright Flyer, by the Wright brothers","title":"Wright Brothers - First Flight"},{"id":9,"filename":"1903p2.jpg","decade":"1900s","source":"Popular Science Monthly Volume 64","info":"Pierre and Maria Skłodowska-Curie in the laboratory with their experimental apparatus, used to detect the ionization of air","title":"Pierre and Marie Curie win Nobel Prize in Physics"},{"id":10,"filename":"1908p1.jpg","decade":"1900s","source":"Library of Congress","info":"Harry Houdini performs a manacled jump from Harvard Bridge in Boston, Massachusetts - photo by John Thurston","title":"Harry Houdini jumps from the Harvard Bridge"},{"id":11,"filename":"1908p2.jpg","decade":"1900s","source":"National Phonograph Co.","info":"Photo of pioneer recording vocal quartet, the

//hey!!!! the quotes and comments and stuff stop working after about 2500 characters (about 12 ids)

const obj = JSON.parse('{"images":[{"id":0,"filename":"1843.jpg","decade":"1840s","source":"The Metropolitan Museum of Art","info":"Former U.S. president John Quincy Adams - early dagguerotype by Philip Haas.","title":"First Presidential Photograph"},{"id":1,"filename":"1862.jpg","decade":"1860s","source":"The Metropolitan Museum of Art","info":"U.S. President Abraham Lincoln visits Antietam Wood - photo by Alexander Gardner","title":"Civil War"},{"id":2,"filename":"1899p2.jpg","decade":"1890s","source":"Wellcome Collection Gallery","info":"Nikola Tesla sitting next to his Tesla coil - photo by Dickinson V. Alley","title":"Nikola Tesla - Tesla Coil"},{"id":3,"filename":"1903p1.jpg","decade":"1900s","source":"Library of Congress","info":"First successful flight of the Wright Flyer, by the Wright brothers","title":"Wright Brothers - First Flight"},{"id":4,"filename":"1936p1.jpg","decade":"1930s","source":"U.S. Farm Security Administration/Office of War Information","info":"Migrant Mother, taken during the Dust Bowl - photo by Dorothea Lange","title":"Dust Bowl"},{"id":5,"filename":"1945p1.jpg","decade":"1940s","source":"National Archives and Records Administration","info":"Slave laborers in the Buchenwald concentration camp are liberated","title":"Holocaust"},{"id":6,"filename":"1969p2.jpg","decade":"1960s","source":"NASA Apollo Archive","info":"Astronaut Edwin E. Aldrin Jr. poses for a photograph during Apollo 11 mission","title":"Apollo 11 Lands on the Moon"},{"id":7,"filename":"1977p2.jpg","decade":"1970s","source":"LucasFilm LTD","info":"Mark Hamill, Carrie Fisher, and Harrison Ford in the film Star Wars Episode IV: A New Hope","title":"Star Wars: A New Hope"},{"id":8,"filename":"1985p2.jpg","decade":"1980s","source":"Universal Pictures","info":"Michael J. Fox and Christopher Lloyd in the film Back to the Future","title":"Back to the Future"},{"id":9,"filename":"1994p1.jpg","decade":"1990s","source":"Columbia","info":"Mariah Careys Merry Christmas promotional photoshoot","title":"Mariah Carey - All I Want For Christmas Is You"},{"id":10,"filename":"2001.jpg","decade":"2000s","source":"National Park Service","info":"September 11 attacks in New York City","title":"9/11 Attacks"},{"id":11,"filename":"2018.jpg","decade":"2010s","source":"UltimateWarrior13","info":"Taylor Swift performing on her Reputation Stadium Tour","title":"Taylor Swift - Shake It Off"}]}')

/*
from fetch_data import result_row

(filename, decade, copyright, info, title) = result_row
img_path = fr"cs100d\module4\app_prototype\popdecades\{filename}"
*/

fetch('./data/db.json')
    .then((response) => response.json())
    .then((json) => console.log(json));

class Main extends React.Component {
    constructor() {
        super()
        //Initial data has no user or counts
        this.state = {filename: null, decade: null, copyright: null, info: null, title: null}
        this.urlbase = 'http://localhost:4000'
    }

    getRandFilename(){
        function randomNumber(min, max) {
            return Math.random() * (max - min) + min;
        }
        
        const rand = randomNumber(0, 11)

        filename = obj[rand].filename

        return rand
    }
    render() {
        rand = getRandFilename()
        return (
            <div className='Main'>

                <div className = 'img'>
                    <img src = 'cs100d\module4\app_prototype\popdecades\{obj[rand].filename}'></img>
                </div>

                <div className = 'desc'>
                    <p>data[rand].title</p>
                    <button type="button">Next Photo</button>
                </div>

                
            </div>
        )
    }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);