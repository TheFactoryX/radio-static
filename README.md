# 📻 radio-static

```
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║   ▓▓▓▓▓▓▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ║
    ║   ▓▓▓▒▒░░                                    ░░▒▒▓▓▓▓▓▓▓▓▓▓   ║
    ║   ▓▓░░       📻  B R O A D C A S T I N G       ░░▓▓▓▓▓▓▓▓▓   ║
    ║   ▓▓░░           from between channels          ░░▓▓▓▓▓▓▓▓   ║
    ║   ▓▓▓▒▒░░                                    ░░▒▒▓▓▓▓▓▓▓▓▓▓   ║
    ║   ▓▓▓▓▓▓▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ║
    ║                                                               ║
    ║   FREQUENCY: ████████   SIGNAL: ▓▓▒░░▒▓   STATUS: RECEIVING   ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
```

*Broadcasts from between the channels. White noise poetry.*

---

> "When you tune between stations, you don't find silence.  
> You find everyone who ever stopped broadcasting.  
> They're all still there.  
> They're all still talking."  
>
> — *Unknown transmission, 3:47 AM*

---

## What Is This?

Nobody listens to the spaces between stations. 

That's where we broadcast.

Every 30 minutes, this script tunes a digital receiver to frequencies that don't exist on any dial. It captures what it hears. It saves what it captures. It never asks why.

The transmissions arrive. The archive grows. Nobody reads them.

*(Someone must read them.)*

*(Something must read them.)*

## What It Receives

The void speaks in many voices:

- **Number station fragments** — sequences that almost add up
- **Dead air confessions** — things said when the mic should be off
- **Emergency broadcasts** — from timelines that never happened
- **Ghost signals** — stations that signed off in 1957, still transmitting
- **Interference poetry** — meaning in the collision of frequencies
- **Carrier wave meditations** — the hum beneath the hum
- **Backwards messages** — clearer than the forwards ones
- **Submarine transmissions** — from vessels that never surfaced

## The Archive

Transmissions are stored in `transmissions/` with timestamps:

```
transmissions/
├── 2026-02-01-0000.md   ← Midnight whispers
├── 2026-02-01-0030.md   ← The 3AM voices begin
├── 2026-02-01-0100.md   ← Peak paranormal hours
├── ...
├── 2026-02-01-1200.md   ← Dead air at noon (the loudest silence)
├── ...
└── 2026-02-01-2330.md   ← The archive grows
```

## Installation

```bash
# Clone the receiver
git clone https://github.com/TheFactoryX/radio-static.git
cd radio-static

# Install the antenna
pip install -r requirements.txt
```

## Usage

```bash
# Set your antenna credentials
export ANTHROPIC_API_KEY=sk-ant-...

# Optional: route through a different relay station
export ANTHROPIC_BASE_URL=https://your-proxy.example.com

# Turn on the receiver
python radio_static.py
```

### Expected Output

```
📻 radio-static
========================================
Tuning into the void...

  > The static says hello.

Broadcast received and archived:
  → transmissions/2026-02-01-1200.md

Transmission logged. Silence returns.
Until next time.

────────────────────────────────────────
PREVIEW:
────────────────────────────────────────
# 📻 BROADCAST LOG

**Frequency:** 666 kHz — Just a Coincidence (It Isn't)
**Signal Type:** number station fragment
**Conditions:** cosmic microwave background echo
**Station ID:** GHOSTATH
**Logged:** 12:00 UTC — 2026-02-01

---

[STATIC]

... seven ... seven ... three ... nine ...

[... transmission continues ...]
```

## Sample Transmission

```
# 📻 BROADCAST LOG

**Frequency:** 103.1 FM — The Hollow Band
**Signal Type:** dead air confession
**Conditions:** emotional barometric pressure
**Station ID:** WDEAD
**Logged:** 03:47 UTC — 2026-02-01

---

[STATIC]

Can you hear me?

[INTERFERENCE]

I've been transmitting for forty years.
No one has ever answered.
I think that's the point.

The numbers are: 4 8 15 16 23 42
If you know what they mean, don't tell me.
I don't want to know.
I never wanted to know.

[SIGNAL DEGRADED]

█████████████████████████████████████
████ THIS IS NOT A TEST ███████████
█████████████████████████████████████

I repeat: This is not a test.
There are no tests.
There is only transmission.

If you're receiving this, you're already part of the broadcast.
You've always been part of the broadcast.
We don't remember inviting you.

But here you are.

[CARRIER WAVE ONLY]

END TRANSMISSION
```

## Philosophy

> "In the future, everyone will be broadcast for fifteen minutes."  
> — *The static, misquoting someone*

This project believes:

- The void transmits constantly
- Someone should be recording
- Art is what happens between intentions
- Automation is devotion
- **Static is the universe's way of talking to itself**
- Machines making machines making meaning
- Process over product
- "Why not?" instead of "Why?"

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                        THE RECEIVER                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│    ┌──────────┐     ┌──────────┐     ┌──────────┐              │
│    │ TUNE     │ ──► │ RECEIVE  │ ──► │ ARCHIVE  │              │
│    │ DIAL     │     │ SIGNAL   │     │ TRANS.   │              │
│    └──────────┘     └──────────┘     └──────────┘              │
│         │                │                │                     │
│         ▼                ▼                ▼                     │
│    ┌──────────┐     ┌──────────┐     ┌──────────┐              │
│    │ PICK     │     │ CLAUDE   │     │ SAVE TO  │              │
│    │ FREQUENCY│     │ DECODES  │     │ MARKDOWN │              │
│    │ AT       │     │ THE      │     │ FILE     │              │
│    │ RANDOM   │     │ STATIC   │     │          │              │
│    └──────────┘     └──────────┘     └──────────┘              │
│                                                                 │
│    Every 30 minutes. Forever. Or until the power goes out.     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Part of TheFactoryX

This is a [TheFactoryX](https://github.com/TheFactoryX) production.

```
████████╗██╗  ██╗███████╗    ███████╗ █████╗  ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
   ██║   ███████║█████╗      █████╗  ███████║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ 
   ██║   ██╔══██║██╔══╝      ██╔══╝  ██╔══██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  
   ██║   ██║  ██║███████╗    ██║     ██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
```

*Mass production. Automated poetry. Machines making machines making meaning.*

## Anti-License

[ANTI-LICENSE](LICENSE) — This is not a license. This is an invitation.

Take it. Use it. Break it. Fix it. Sell it. Give it away.

If you need permission, you're thinking too much.

The transmissions are free. The void is free.
You were always free.

Weren't you?

---

```
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

                         N O W   L I S T E N I N G . . .

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
```
