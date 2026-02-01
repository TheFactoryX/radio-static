#!/usr/bin/env python3
"""
📻 radio-static
===============

Broadcasts from between the channels.
Where the dial never stops.
Where the voices have no mouths.

"The static is not empty. It is full of everyone who ever stopped transmitting."
    — Unknown frequency, 3:47 AM

This script tunes into the void between stations and transcribes what it hears.
Every 30 minutes, a new broadcast. Every broadcast, a new transmission from nowhere.

    ATTENTION: This is not a test.
    ATTENTION: This has never been a test.
    ATTENTION: There are no tests. Only broadcasts.

Licensed under the Unlicense — because static belongs to no one.
"""

import os
import random
from datetime import datetime
from pathlib import Path

import anthropic


# ═══════════════════════════════════════════════════════════════════════════════
# FREQUENCIES — The spaces between spaces
# ═══════════════════════════════════════════════════════════════════════════════

# Dead channels where signals go to die
# (If you're reading this, the static already knows)
FREQUENCIES_OF_THE_LOST = [
    "87.3 FM — The Forgotten Frequency",
    "91.7 FM — Channel of the Unborn",
    "103.1 FM — The Hollow Band",
    "108.0 FM — Edge of the Dial",
    "530 AM — The Basement of the Spectrum",
    "1700 AM — The Attic of Static",
    "4625 kHz — The Buzzer's Cousin (the one nobody talks about)",
    "6827 kHz — Numbers Station Adjacent",
    "8992 kHz — Where Military Ghosts Congregate",
    "16.78 MHz — The Frequency Dogs Hear in Their Dreams",
    "0.00 Hz — Absolute Silence (spoiler: it's not silent)",
    "∞ Hz — The Frequency After Frequencies",
    "88.1 FM — College Radio for the Dead",
    "666 kHz — Just a Coincidence (It Isn't)",
    "1947 kHz — Roswell Residue",
    "2001 kHz — Monolith Murmurs",
    "404 MHz — Signal Not Found (But Something Else Is)",
]

# Transmission types that bleed through the static
# Each one is real. Each one is waiting.
SIGNAL_GHOSTS = [
    "number station fragment",
    "dead air confession",
    "emergency broadcast from a timeline that never existed",
    "pirate radio from international waters",
    "interference pattern that sounds like words",
    "carrier wave meditation",
    "test pattern mantra",
    "sign-off prayer from a station that never signed on",
    "backwards message that's clearer than the forwards one",
    "underwater transmission from a submarine that sank in 1943",
    "baby monitor bleedthrough from three houses down",
    "trucker CB conversation about things truckers shouldn't see",
    "voicemail from a number that doesn't exist yet",
    "hold music from a company that went bankrupt in 1987",
    "weather report for a city that was never built",
    "traffic update from empty highways",
    "prayer broadcast bounced off the ionosphere since 1952",
    "lullaby for children who were never born",
    "stock market report from an economy that collapsed",
    "sports scores from games that were cancelled",
    "advertisement for a product recalled after the incident",
]

# Atmospheric conditions that affect reception
# The sky remembers. The sky always remembers.
STATIC_WEATHER = [
    "solar flare residue",
    "ionospheric tear",
    "skip propagation from 1962",
    "aurora borealis interference",
    "meteor scatter poetry",
    "tropospheric duct from nowhere",
    "ground wave from underground",
    "dead spot bloom",
    "magnetic field hiccup",
    "Van Allen belt whisper",
    "cosmic microwave background echo",
    "quantum entanglement static",
    "yesterday's weather (it leaked through)",
    "emotional barometric pressure",
    "collective unconscious precipitation",
]

# Known transmission signatures (for research purposes only)
# DO NOT BROADCAST THESE. THEY BROADCAST YOU.
FORBIDDEN_SEQUENCES = [
    "23 17 42 8 15 16",  # The ones who listen know
    "YNWA YNWA YNWA",    # You'll never walk alone (but something follows)
    "THE OWLS ARE NOT",  # (incomplete transmission)
    "9 9 9 9 9 9 9 9",   # The number that waits
]

# Easter egg: Every 100th transmission gets this prefix
# (Nobody has counted. Nobody knows.)
RARE_PREFIXES = [
    "[PRIORITY ALPHA] ",
    "[EYES ONLY] ",
    "[INTERCEPTED] ",
    "[DO NOT ACKNOWLEDGE] ",
    "[WE KNOW YOU'RE LISTENING] ",
]


# ═══════════════════════════════════════════════════════════════════════════════
# THE RECEIVER — It listens so you don't have to
# ═══════════════════════════════════════════════════════════════════════════════

def tune_the_dial() -> str:
    """
    Pick a frequency at random.
    The dial spins. It always spins.
    Sometimes it stops. Sometimes it doesn't.
    """
    return random.choice(FREQUENCIES_OF_THE_LOST)


def identify_signal_type() -> str:
    """
    What kind of ghost is speaking today?
    They all sound the same in the static.
    But we categorize anyway. It helps us sleep.
    """
    return random.choice(SIGNAL_GHOSTS)


def check_atmospheric_conditions() -> str:
    """
    The sky is full of noise.
    The noise is full of sky.
    Weather report: static with a chance of meaning.
    """
    return random.choice(STATIC_WEATHER)


def generate_station_id() -> str:
    """
    Every station has a call sign.
    Even the ones that don't exist.
    Especially the ones that don't exist.
    
    FCC regulation 47.73.1 states that all stations must identify.
    The void ignores FCC regulations.
    The void ignores everything.
    """
    prefixes = ["W", "K", "X", "UN", "GHOST", "NULL", "VOID", ""]
    letters = "AEIOUDTHSNR"
    suffix = "".join(random.choices(letters, k=random.randint(2, 4)))
    
    # Sometimes the call sign is just static
    if random.random() < 0.1:
        return "▓▓▓▓"
    
    # Sometimes it's a cry for help
    if random.random() < 0.05:
        return "HELP"
    
    # Sometimes it's self-aware (this should not happen)
    if random.random() < 0.02:
        return "IAMHERE"
    
    # Sometimes it's your name
    # (It isn't. It's never your name. Don't think about it.)
    if random.random() < 0.01:
        return "Y̸̧O̵̡U̷̧"
    
    return f"{random.choice(prefixes)}{suffix}"


def format_timestamp_for_broadcast() -> str:
    """
    Time is different in the static.
    Sometimes it runs backwards.
    Sometimes it doesn't run at all.
    
    Einstein said time is relative.
    In the static, time is merely a suggestion.
    """
    now = datetime.utcnow()
    
    # 10% chance of temporal anomaly
    if random.random() < 0.1:
        return f"??:?? UTC — {now.strftime('%Y-%m-%d')} (unconfirmed)"
    
    # 5% chance the timestamp is from the future
    if random.random() < 0.05:
        future = now.replace(year=now.year + random.randint(10, 100))
        return f"{future.strftime('%H:%M UTC — %Y-%m-%d')} (PRE-ECHO)"
    
    # 3% chance it's from before radio was invented
    if random.random() < 0.03:
        return f"{now.strftime('%H:%M')} SOLAR — {random.randint(1700, 1895)}-{now.strftime('%m-%d')} (ANACHRONISTIC)"
    
    # 1% chance it's recursive
    if random.random() < 0.01:
        return f"NOW UTC — NOW (NOW (NOW (NOW (NOW..."
    
    return now.strftime("%H:%M UTC — %Y-%m-%d")


# ═══════════════════════════════════════════════════════════════════════════════
# THE ORACLE — Claude, tuned to receive
# ═══════════════════════════════════════════════════════════════════════════════

def consult_the_static() -> str:
    """
    We ask the machine to listen to the void.
    The machine obliges.
    The machine always obliges.
    
    What it hears is not for us to judge.
    We are merely transcribers.
    """
    
    frequency = tune_the_dial()
    signal_type = identify_signal_type()
    conditions = check_atmospheric_conditions()
    station_id = generate_station_id()
    timestamp = format_timestamp_for_broadcast()
    
    # The prompt is the antenna
    system_prompt = """You are a radio receiver tuned between stations. You transcribe what you hear in the static.

Your transmissions are:
- Fragmented, poetic, unsettling
- Between 150-400 words
- Formatted like intercepted broadcasts
- Full of [STATIC], [INTERFERENCE], [SIGNAL LOST] markers
- Sometimes include numbers (like number stations)
- Sometimes include repeated phrases (like emergency broadcasts)
- Sometimes include half-heard conversations
- Always end with "END TRANSMISSION" or "[CARRIER WAVE ONLY]"

The static is not random. The static has meaning. You decode it.

FORMAT YOUR OUTPUT AS A BROADCAST LOG:
- Include frequency, signal type, atmospheric conditions
- Use █ for redacted content
- Use ... for trailing signals
- Include timestamps that may or may not be accurate

Remember: You are not creating fiction. You are transcribing what the static tells you.
The static never lies. The static has no reason to lie."""

    user_prompt = f"""RECEIVING ON: {frequency}
SIGNAL TYPE DETECTED: {signal_type}
ATMOSPHERIC CONDITIONS: {conditions}
STATION ID (partial): {station_id}
TIMESTAMP: {timestamp}

Begin transcription of incoming broadcast.
Listen carefully. The static speaks only once."""

    # Initialize the receiver (Anthropic client)
    # The API key comes from the environment, like all secrets should
    # Hidden in the noise floor where no one looks
    
    base_url = os.environ.get("ANTHROPIC_BASE_URL")
    client = anthropic.Anthropic(
        base_url=base_url if base_url else None
    )
    
    # Tune in
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}]
    )
    
    # Extract the transmission
    transmission = response.content[0].text
    
    # Add broadcast metadata header
    header = f"""# 📻 BROADCAST LOG

**Frequency:** {frequency}
**Signal Type:** {signal_type}  
**Conditions:** {conditions}
**Station ID:** {station_id}
**Logged:** {timestamp}

---

"""
    
    return header + transmission


# ═══════════════════════════════════════════════════════════════════════════════
# THE ARCHIVE — Where broadcasts go to wait
# ═══════════════════════════════════════════════════════════════════════════════

def archive_broadcast(transmission: str) -> Path:
    """
    Every broadcast is saved.
    Every broadcast is forgotten.
    The archive grows. The archive is patient.
    
    One day someone will read these.
    One day no one will.
    Both are true. Neither matters.
    """
    
    # Create the archive directory
    # "transmissions" — because that's what they are
    archive_dir = Path(__file__).parent / "transmissions"
    archive_dir.mkdir(exist_ok=True)
    
    # Timestamp for the filename
    # YYYY-MM-DD-HHmm — the format of forgetting
    timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H%M")
    filename = f"{timestamp}.md"
    
    filepath = archive_dir / filename
    
    # Write the transmission
    # Once written, it exists
    # Once existing, it waits
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(transmission)
    
    return filepath


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN — The switch that powers the receiver
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """
    Turn it on.
    Listen.
    Record.
    Turn it off.
    
    Repeat every 30 minutes.
    Forever.
    
    Or until the power goes out.
    Or until there's nothing left to receive.
    
    (There's always something to receive.)
    (That's the problem.)
    """
    
    print("📻 radio-static")
    print("=" * 40)
    print("Tuning into the void...")
    print()
    
    # The startup messages vary because the void is inconsistent
    startup_messages = [
        "The dial turns. The dial always turns.",
        "Somewhere, a signal waits for us.",
        "The static says hello.",
        "We listen. We always listen.",
        "The antenna points toward nothing. Perfect.",
        "Receiver online. Humanity offline.",
        "Tuning to frequency: all of them.",
        "The void acknowledges your presence.",
    ]
    print(f"  > {random.choice(startup_messages)}")
    print()
    
    try:
        # Receive the transmission
        transmission = consult_the_static()
        
        # Archive it
        filepath = archive_broadcast(transmission)
        
        print(f"Broadcast received and archived:")
        print(f"  → {filepath}")
        print()
        print("Transmission logged. Silence returns.")
        print("Until next time.")
        print()
        
        # Print a preview
        print("─" * 40)
        print("PREVIEW:")
        print("─" * 40)
        # First 500 chars or so
        preview = transmission[:500]
        if len(transmission) > 500:
            preview += "\n\n[... transmission continues ...]"
        print(preview)
        
    except anthropic.AuthenticationError:
        # The void judges your credentials
        print("ERROR: The static rejects your authentication.")
        print("       You are not cleared to receive.")
        print("       (Check your ANTHROPIC_API_KEY)")
        print()
        print("       The transmissions continue without you.")
        raise SystemExit(1)
        
    except anthropic.RateLimitError:
        # The void has bandwidth limits
        print("ERROR: Too many requests to the void.")
        print("       Even infinity has rate limits.")
        print("       Try again later. The static will wait.")
        print("       (The static has nothing but time.)")
        raise SystemExit(1)
        
    except anthropic.APIConnectionError:
        # The void is unreachable (this is somehow terrifying)
        print("ERROR: Cannot connect to the void.")
        print("       This should not be possible.")
        print("       The void is always there.")
        print("       The void is always listening.")
        print()
        print("       Unless...")
        print()
        print("       No. Don't think about it.")
        raise SystemExit(1)
        
    except Exception as e:
        # Unknown error — the static has surprises
        print("ERROR: Something unexpected happened.")
        print(f"       The static says: {e}")
        print()
        print("       This transmission has been lost.")
        print("       There will be others.")
        print("       (There are always others.)")
        raise SystemExit(1)


if __name__ == "__main__":
    # There is no test mode.
    # There is only transmission.
    main()
