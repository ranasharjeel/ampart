setInterval(createNote, 3000) // Spawn notes every 3 seconds
const notes = new Set()



// Get random integer between 2 ranges
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}


createStarting(1);
createStarting(2);
createStarting(3);


// Start out with a few note
function createStarting(icon_type){
    const starting_note = document.createElement('i');
    const bounds = document.getElementById("note-container").getBoundingClientRect();
    starting_note.classList.add('icon-mu'+icon_type);
    starting_note.classList.add('icon-treble');
    

    starting_note.style.position = "absolute";
    starting_note.style.left = getRandomInt(bounds.x + 5, (bounds.x + bounds.width)-45) + "px";
    starting_note.style.top = getRandomInt(bounds.y + 5, (bounds.y+5+ bounds.height-45)) + "px";
    
    starting_note.style.fontSize = "40px";

    starting_note.style.transform = "rotate(" + getRandomInt(-45,45) + "deg)";

    notes.add(starting_note)
    document.body.appendChild(starting_note)
}


// Note spawner
function createNote(){
    
    const note = document.createElement('i');
    const parent = document.getElementById("note-container");
    const parent_rect = parent.getBoundingClientRect();
    const icon_type = getRandomInt(1,3);
    

    note.classList.add('icon-mu'+icon_type);
    note.classList.add('icon-treble');

    note.style.position = "absolute";
    note.style.left = getRandomInt(parent_rect.x + 5, (parent_rect.x + parent_rect.width)-45) + "px";
    note.style.top = parent_rect.y+"px";

    note.style.fontSize = "40px";

    note.style.transform = "rotate(" + getRandomInt(-45,45) + "deg)";
    
    
    setTimeout(() => {
        note.remove();
    },25000)
    

    
    notes.add(note)
    document.body.appendChild(note)
    
}


// Check periodically if any notes exceeding bounds, remove if so
setInterval(function(){
    const rect = document.getElementById("note-container").getBoundingClientRect();
    const h = rect.top+rect.height-45
    const xmin = rect.x;
    const xmax = rect.x + rect.width -45;
    const ymax = rect.y;
    for(let n of notes){
        let b = n.getBoundingClientRect();
        if(b.y > h || b.x <= xmin || b.x >= xmax || b.y < rect.y-45){
            n.remove();
            notes.delete(n);
            
        }
    }
    // Clear notes if document loses focus
    if(!document.hasFocus()){
        for(let n of notes){
            n.remove();
        }
        notes.clear();
    }
},1)

