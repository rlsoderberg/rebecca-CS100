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
var glossary = {"glossary": [{"id": 0,"filename": "spinning_capybara.gif","decade": "2020s","source": "Nivora Animation","info": "The capybara is spinning","title": "Spinning Capybara"},{"id": 1,"filename": "bunny_eating_lettuce.gif","decade": "2020s","source": "zoomzeu","info": "The bunny is eating lettuce","title": "Lettuce Bunny"},{"id": 2,"filename": "man_with_giant_backpack.gif","decade": "2010s","source": "heather_8lim","info": "This man has a giant backpack","title": "Backpack Man"},{"id": 3,"filename": "spider_aliens.jpg","decade": "2020s","source": "Gboard Stickers","info": "This spider is getting abducted by aliens","title": "Spider Abduction"}]}
//i saw this cool thing, but, like, that didn't help!!!
/*
try {
    JSON.parse(glossary); 
    console.log(glossary);
}
    catch (e) {
    console.log(e); 
}
    */
/*
var jsontext = '{"firstname":"Jesper","surname":"Aaberg","phone":["555-0100","555-0120"]}'
var contact = JSON.parse(jsontext);
*/
//>>>latest one const obj = JSON.parse('{"id":0,"filename":"1843.jpg","decade":"1840s","source":"The Metropolitan Museum of Art","info":"Former U.S. president John Quincy Adams - early dagguerotype by Philip Haas.","title":"First Presidential Photograph"},{"id":1,"filename":"1862.jpg","decade":"1860s","source":"The Metropolitan Museum of Art","info":"U.S. President Abraham Lincoln visits Antietam Wood - photo by Alexander Gardner","title":"Civil War"},{"id":2,"filename":"1899p2.jpg","decade":"1890s","source":"Wellcome Collection Gallery","info":"Nikola Tesla sitting next to his Tesla coil - photo by Dickinson V. Alley","title":"Nikola Tesla - Tesla Coil"},{"id":3,"filename":"1903p1.jpg","decade":"1900s","source":"Library of Congress","info":"First successful flight of the Wright Flyer, by the Wright brothers","title":"Wright Brothers - First Flight"},{"id":4,"filename":"1936p1.jpg","decade":"1930s","source":"U.S. Farm Security Administration/Office of War Information","info":"Migrant Mother, taken during the Dust Bowl - photo by Dorothea Lange","title":"Dust Bowl"},{"id":5,"filename":"1945p1.jpg","decade":"1940s","source":"National Archives and Records Administration","info":"Slave laborers in the Buchenwald concentration camp are liberated","title":"Holocaust"},{"id":6,"filename":"1969p2.jpg","decade":"1960s","source":"NASA Apollo Archive","info":"Astronaut Edwin E. Aldrin Jr. poses for a photograph during Apollo 11 mission","title":"Apollo 11 Lands on the Moon"},{"id":7,"filename":"1977p2.jpg","decade":"1970s","source":"LucasFilm LTD","info":"Mark Hamill, Carrie Fisher, and Harrison Ford in the film Star Wars Episode IV: A New Hope","title":"Star Wars: A New Hope"},{"id":8,"filename":"1985p2.jpg","decade":"1980s","source":"Universal Pictures","info":"Michael J. Fox and Christopher Lloyd in the film Back to the Future","title":"Back to the Future"},{"id":9,"filename":"1994p1.jpg","decade":"1990s","source":"Columbia","info":"Mariah Careys Merry Christmas promotional photoshoot","title":"Mariah Carey - All I Want For Christmas Is You"},{"id":10,"filename":"2001.jpg","decade":"2000s","source":"National Park Service","info":"September 11 attacks in New York City","title":"9/11 Attacks"},{"id":11,"filename":"2018.jpg","decade":"2010s","source":"UltimateWarrior13","info":"Taylor Swift performing on her Reputation Stadium Tour","title":"Taylor Swift - Shake It Off"}')
//const obj = JSON.parse('{"images":[{"id":0,"filename":"1843.jpg","decade":"1840s","source":"The Metropolitan Museum of Art","info":"Former U.S. president John Quincy Adams - early dagguerotype by Philip Haas.","title":"First Presidential Photograph"},{"id":1,"filename":"1862.jpg","decade":"1860s","source":"The Metropolitan Museum of Art","info":"U.S. President Abraham Lincoln visits Antietam Wood - photo by Alexander Gardner","title":"Civil War"},{"id":2,"filename":"1899p2.jpg","decade":"1890s","source":"Wellcome Collection Gallery","info":"Nikola Tesla sitting next to his Tesla coil - photo by Dickinson V. Alley","title":"Nikola Tesla - Tesla Coil"},{"id":3,"filename":"1903p1.jpg","decade":"1900s","source":"Library of Congress","info":"First successful flight of the Wright Flyer, by the Wright brothers","title":"Wright Brothers - First Flight"},{"id":4,"filename":"1936p1.jpg","decade":"1930s","source":"U.S. Farm Security Administration/Office of War Information","info":"Migrant Mother, taken during the Dust Bowl - photo by Dorothea Lange","title":"Dust Bowl"},{"id":5,"filename":"1945p1.jpg","decade":"1940s","source":"National Archives and Records Administration","info":"Slave laborers in the Buchenwald concentration camp are liberated","title":"Holocaust"},{"id":6,"filename":"1969p2.jpg","decade":"1960s","source":"NASA Apollo Archive","info":"Astronaut Edwin E. Aldrin Jr. poses for a photograph during Apollo 11 mission","title":"Apollo 11 Lands on the Moon"},{"id":7,"filename":"1977p2.jpg","decade":"1970s","source":"LucasFilm LTD","info":"Mark Hamill, Carrie Fisher, and Harrison Ford in the film Star Wars Episode IV: A New Hope","title":"Star Wars: A New Hope"},{"id":8,"filename":"1985p2.jpg","decade":"1980s","source":"Universal Pictures","info":"Michael J. Fox and Christopher Lloyd in the film Back to the Future","title":"Back to the Future"},{"id":9,"filename":"1994p1.jpg","decade":"1990s","source":"Columbia","info":"Mariah Careys Merry Christmas promotional photoshoot","title":"Mariah Carey - All I Want For Christmas Is You"},{"id":10,"filename":"2001.jpg","decade":"2000s","source":"National Park Service","info":"September 11 attacks in New York City","title":"9/11 Attacks"},{"id":11,"filename":"2018.jpg","decade":"2010s","source":"UltimateWarrior13","info":"Taylor Swift performing on her Reputation Stadium Tour","title":"Taylor Swift - Shake It Off"}');
//just checking whether i put in too many quotation marks. i don't think that's it???
//const obj = JSON.parse('{images:[{id:0,filename:"1843.jpg",decade:"1840s",source:"The Metropolitan Museum of Art",info:"Former U.S. president John Quincy Adams - early dagguerotype by Philip Haas.",title:"First Presidential Photograph"},{id:1,filename:"1862.jpg",decade:"1860s",source:"The Metropolitan Museum of Art",info:"U.S. President Abraham Lincoln visits Antietam Wood - photo by Alexander Gardner",title:"Civil War"}]};') 
//const obj = JSON.parse('{"name":"John", "age":30, "city":"New York"}');
//person = {name:"John", age:31, city:"New York"};
/*
from fetch_data import result_row

(filename, decade, source, info, title) = result_row
img_path = fr"cs100d\module4\app_prototype\popdecades\{filename}"
*/
/*
fetch('./data/db.json')
    .then((response) => response.json())
    .then((json) => console.log(json));
*/

class Main extends React.Component {
    constructor() {
        super()
        //Initial data has no user or counts
        this.urlbase = 'http://localhost:4000'
        this.state = {rand:0, id: 0, filename:'', decade:'', source:'', info:'', title:''}
    }

    getRandFilename(){
        function getRandomInt(min, max) {
            return Math.random() * (max - min) + min;
        }

        var rand = getRandomInt(11)
        
        this.setState({...this.state, rand: rand})

        //const obj = obj[rand].parse()
/* not even going to finish this one!!!
        var id=a.getEmailBasicData;
        var filename=a.getEmailDocumentData;
        var decade=a.getEmailParticipantData;
        var source=a.getEmailBasicData;
        var info=a.getEmailDocumentData;
        var title=a.getEmailParticipantData;
        */
/*
        (id, filename, decade, source, info, title) = obj[rand]

        this.setState({id:id, filename:filename, decade:decade, source:source, info:info, title:title})
*/
    }
    fillTable () {
        //console.log(glossary[0])
    }
    render() {
        /*unsuccessful change attempt
        const {filename, title} = this.state
        //var str = JSON.stringify(contact);
        var id = filename
        console.log(id)
        */
        const {filename, title} = this.state
        //var str = JSON.stringify(contact);
        //var id = str[1]
        //console.log(id)
        console.log(glossary[0])
        console.log(glossary)
        console.log(JSON.stringify(glossary))
        return (
            <div className='Main'>

                <div className = 'img'>
                    <img src = '.\popdecades\{filename}'></img>
                    
                </div>

                <div className = 'desc'>
                    <p>{title}</p>
                    <button type="button" /*onClick={this.getRandFilename.bind(this)}*/>Next Photo</button>
                </div>

                
            </div>
        )
    }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);