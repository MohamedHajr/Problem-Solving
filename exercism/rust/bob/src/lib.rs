pub fn reply(message: &str) -> &str {

    let message = message.trim();

    //Message is empty
    if message == "" {
        return "Fine. Be that way!"
    }

    //Filter message from non alphabetic chars 
    let filtered_chars = message.chars().filter(|x| x.is_alphabetic()).collect::<String>();

    let is_yelling = filtered_chars != ""  && filtered_chars.chars().all(char::is_uppercase); 
    let is_question = message.ends_with('?');

    match (is_question, is_yelling) {
        (true, true) => "calm down, i know what i'm doing!",
        (true, false) => "Sure.",
        (false, true) => "Whoa, chill out!",
        (_, _) => "Whatever.",
    }
}
