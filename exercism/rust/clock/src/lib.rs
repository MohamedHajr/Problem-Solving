use std::fmt;

#[derive(Debug, PartialEq)]
pub struct Clock{
    minutes: i32,
}

fn hrs_to_mins(hours: i32) -> i32 {
    if hours >= 0 {
      (hours % 24) * 60
    } else {
      (24 - (hours.abs() % 24)) * 60
    }
}

fn calc_mins(minutes: i32) -> i32 {
    if minutes > 0 {
        minutes % 60
    } else {
        let pos_mins = minutes.abs();
        match pos_mins % 60 {
            0 => 0,
            _ => 60 - (pos_mins % 60)
        }
    }
}

fn calc_hours(minutes: i32) -> i32  {
     if minutes > 0 {
        (minutes / 60) % 24
    } else {
        let pos_mins = minutes.abs();
        let mut hours = 24 - ((pos_mins / 60) % 24);
        if pos_mins % 60 > 0 {
          hours -= 1;  
        } 
        hours
    }
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        Clock {
            minutes: (minutes + hrs_to_mins(hours))
        }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Clock {
            minutes: (self.minutes + minutes)
        }
    }
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let hrs = calc_hours(self.minutes);
        let mins = calc_mins(self.minutes);
        let hours = if hrs < 10 {
            format!("0{}", hrs)
        } else {
            hrs.to_string()
        };
        let minutes = if mins < 10 {
            format!("0{}", mins)
        } else {
            mins.to_string()
        };
        write!(f, "{}:{}", hours, minutes)
    }
}
