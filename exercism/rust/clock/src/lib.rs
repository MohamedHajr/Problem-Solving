use std::fmt;

fn calculate_clock(hours: i32, minutes: i32) -> (i32, i32){
    let mut hours = if hours >= 0 {
      hours % 24
    } else {
      24 - (hours.abs() % 24)
    };
    
    let minutes: i32 = if minutes > 0 {
        if minutes >= 60 {
            hours += minutes / 60;
            hours %= 24;
        }
        minutes % 60
    } else {
        let pos_mins = minutes.abs();
        //add or substract additonal minutes than 60 to hours
        hours -= pos_mins / 60; 
        if pos_mins % 60 > 0 {
          hours -= 1;  
        }
        hours = hours % 24;
        if hours < 0 {
            hours += 24
        }
        match pos_mins % 60 {
            0 => 0,
            _ => 60 - (pos_mins % 60)
        }
    };
    (hours, minutes)
}

#[derive(Debug)]
pub struct Clock{
    hours: i32,
    minutes: i32,
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        let (hours, minutes) = calculate_clock(hours, minutes);
        Clock {
            hours,
            minutes
        }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        let (hours, minutes) = calculate_clock(self.hours, self.minutes + minutes);
        Clock {
            hours,
            minutes
        }
    }
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let hours = if self.hours < 10 {
            format!("0{}", self.hours)
        } else {
            self.hours.to_string()
        };
        let minutes = if self.minutes < 10 {
            format!("0{}", self.minutes)
        } else {
            self.minutes.to_string()
        };
        write!(f, "{}:{}", hours, minutes)
    }
}

impl PartialEq for Clock {
    fn eq(&self, other: &Clock) -> bool {
        self.hours == other.hours && self.minutes == other.minutes
    }
}
