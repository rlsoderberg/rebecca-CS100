import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class Main extends React.Component {
    constructor() {
        super()
        //Initial data has no user or counts
        this.urlbase = 'http://localhost:4000'
        this.state = {rand:0, id: 0, filename:'', decade:'', source:'', info:'', title:''}
    }

    @app.route('/login', methods=['POST'])
    def login():

        //ok, so i'm looking at the login route
        //ooh, what if I use my python data fetcher to fetch my data, and then... well... then i would have to get mysql to work. what am i doing???
        //i couldn't start the mysql service because the system cannot find the file specified!!!
        //should i... reinstall mysql again???
        //should i look for alternatives to pymysql???
        //i'm just going to try mariadb...
        //now i have to remember how to use mariadb!!!
        //luckily, i think this is the video tutorial i used last time...
        //wait, surely i have run into this before. program files has a space in it????
        //i think it worked putting it in quotes?
        //noooo. this isn't working. hopefully it's not outdated!!!
        //omg, this newer tutorial recommends docker and stackbricks. rly??? y so many applications!!! what is all this stuff???
        //no, you know what, let me try installing the version of mariadb that's in the tutorial
        //omg, it's still not recognizing mysql!!! why am i having soooo many problems with mysql
        //well, at the very least, mariadb is easier to reinstall than mysql
        //let me try this again with the extra applications...
        //omg!!! i tried to start my database in stackbricks but the starting container failed!!!
        //it kind of looks like it's complaining about something else using port 3306??? i mean, yeah, that's where i put my mariadb, right???
        //ok, that was silly, i changed to port 3307
        //ok, i created my database, i'll try to get server.py working tomorrow


        return jsonify({"id": 0,"filename": "spinning_capybara.gif","decade": "2020s","source": "Nivora Animation","info": "The capybara is spinning","title": "Spinning Capybara"},{"id": 1,"filename": "bunny_eating_lettuce.gif","decade": "2020s","source": "zoomzeu","info": "The bunny is eating lettuce","title": "Lettuce Bunny"},{"id": 2,"filename": "man_with_giant_backpack.gif","decade": "2010s","source": "heather_8lim","info": "This man has a giant backpack","title": "Backpack Man"},{"id": 3,"filename": "spider_aliens.jpg","decade": "2020s","source": "Gboard Stickers","info": "This spider is getting abducted by aliens","title": "Spider Abduction"})
//i saw this cool thing, but, like, that didn't help!!!
    
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