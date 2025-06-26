# A small project to learn OOP implementation

_____________________________________________________________________
current data in library:
BOOKS:
The Great Gatsby by F. Scott Fitzgerald (ID: 001)
To Kill a Mockingbird by Harper Lee (ID: 002)
Dune by Frank Herbert (ID: 003)
Everything Sad Is Untrue by Daniel Nayeri (ID: 004)
The Hobbit by J.R.R. Tolkien (ID: 005)
The Martian by Andy Weir (ID: 006)

COMICS:
Omniscient Reader by Sing N Song (ID: 007)
My Broken Mariko by Waka Hirako (ID: 008)
Noblesse by Son Jeho (ID: 009)
Solo Leveling by Chu-Gong (ID: 010)
Death Note by Tsugumi Ohba (ID: 011)

DVDS:
The Promised Neverland directed by Mamoru Kanbe (ID: 012)
91 Days directed by Hiro Kaburagi (ID: 013)
Parasite directed by Bong Joon-ho (ID: 014)
Oldboy directed by Park Chan-wook (ID: 015)

MEMBERS:
Nanami kento (ID: 218)
Siachin (ID: 119)

GUESTS:
[Auto-generated as "GUEST_XXX" when created]


_________________________________________________________________________________
# Library Management System

## Overview
A Python-based library management system that handles books, comics, DVDs, members, and guest users with checkout/return functionality.

## Features

### Item Management
- Add books, comics, and DVDs
- Track availability status (checked out/available)
- Store creator information (authors/artists/directors)
- Unique IDs for all items

### User Management
- Register members
- Temporary guest accounts
- Track borrowed items
- Different borrowing limits:
  - Members: 5 items for 14 days
  - Guests: 1 item for 7 days

### Core Operations
- Check out items
- Return items
- Search functionality
- Display all items/users

## Sample Data
Pre-loaded with:
- 6 books including:
  - *The Great Gatsby*
  - *Dune* 
  - *The Martian*
- 5 comics including:
  - *Omniscient Reader*
  - *Death Note*
- 4 DVDs including:
  - *Parasite*
  - *Oldboy*
- 2 pre-registered members

## Usage
Run `library-management.py` to access the menu:


