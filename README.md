# WFH Tax Calendar Calculator

A browser-based tool to help Australian taxpayers calculate their work-from-home hours using Google Calendar data. Built with PyScript and designed to work entirely in the browser with no server-side processing.

## Features

- Import Google Calendar ICS files containing work-from-home records
- Calculate total WFH hours for Australian financial years
- Support for recurring calendar events
- Privacy-focused: all processing happens in your browser

## How it Works

1. Create a dedicated calendar in Google Calendar for tracking WFH hours
2. Add events for your work from home days (recurring events supported)
3. Export the calendar as an ICS file
4. Upload the file to this tool
5. Select the financial year of interest
6. View your total WFH hours

## Local Development

### Prerequisites

- Modern web browser
- Local web server or pyscript.com

## Privacy

This tool processes all data locally in your browser. No personal information or calendar data is transmitted to any external servers.

## Disclaimer

This tool is provided as-is with no guarantees as to accuracy nor reliability, and is not affiliated with the Australian Tax Office (ATO). Users are responsible for ensuring the accuracy of their records and calculations.

## Acknowledgments

- [recurring-ical-events](https://github.com/niccokunzmann/python-recurring-ical-events) library by Nicco Kunzmann
- [PyScript](https://pyscript.net/) for enabling Python in the browser
- [Pico CSS](https://picocss.com/) for minimal CSS framework

## Contact

Roger Barnes - roger+wfhtaxcalc@mindsocket.com.au
