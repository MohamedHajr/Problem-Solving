use chrono::{DateTime, Utc, Duration};

// Returns a Utc DateTime one billion seconds after start.
pub fn after(start: DateTime<Utc>) -> DateTime<Utc> {
    const SECONDS: i64 = 1e9 as i64; 
    start + Duration::seconds(SECONDS)
}
