-- This script retrieves scores and names from second_table,
-- excluding rows with null names.
-- The database name is passed as an argument.
-- Records are ordered by score (descending).
SELECT score, name
FROM second_table
WHERE name IS NOT NULL  -- Filter out rows with null names
ORDER BY score DESC;  -- Sort by score (highest first)
