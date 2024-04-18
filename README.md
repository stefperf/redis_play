# Redis Python3 Demo

This project demonstrates various Redis functionalities using Python3, showcasing how to interact with Redis for different types of data structures and operations.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 3.6 or later.
* You have Docker installed on your machine.

## Installation

Clone this repository to your local machine:

    git clone https://your-repository-url-here.git
    cd your-repository-directory

Install the required Python packages:

    pip install redis

## Usage

To run the demo script, execute:

    python redis_play.py

## Features

This project includes demonstrations of the following Redis functionalities:
- **Strings**: Saving, modifying, and retrieving string values.
- **Lists**: Operations on lists including pushing and setting elements.
- **Hashes**: Creating and modifying hash maps.
- **Sets**: Managing sets including adding and removing elements.
- **Sorted Sets**: Using sorted sets to maintain sorted data.
- **HyperLogLog**: Estimating the cardinality of a set.
- **Geospatial Indexes**: Managing geospatial data and queries.
- **Streams**: Working with Redis streams for messaging.
- **Key Expiration**: Setting a specific expiration time for individual keys.
- **Data Persistence**: Persisting data for recovery both as RDB snapshots and more frequently as AppendOnlyFile.

Each feature is showcased in the `redis_demo()` function, which is well-commented to explain the purpose and usage of each Redis command.

## Contributing

Contributions to this project are welcome. To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a pull request.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the LICENSE.md file for details.
