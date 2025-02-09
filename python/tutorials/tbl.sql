CREATE TABLE `category` (
   `id` INTEGER NOT NULL PRIMARY KEY,
   `name` varchar(255) NOT NULL,
   `game` INTEGER NOT NULL,
   `round` INTEGER NOT NULL,
   `boardPosition` INTEGER DEFAULT NULL
);

CREATE TABLE `clue` (
   `id` INTEGER NOT NULL PRIMARY KEY,
   `text` varchar(255) NOT NULL,
   `game` INTEGER NOT NULL,
   `category` INTEGET NOT NULL,
   `value` INTEGER DEFAULT NULL,
   `answer` varchar(255) NOT NULL,
   `isDD` INTEGER NOT NULL,
   `pickIndex` INTEGER DEFAULT NULL
);
