## 620. Not Boring Movies

Table: Cinema

> +----------------+----------+<br/>
> | Column Name    | Type     |<br/>
> +----------------+----------+<br/>
> | id             | int      |<br/>
> | movie          | varchar  |<br/>
> | description    | varchar  |<br/>
> | rating         | float    |<br/>
> +----------------+----------+<br/>
> id is the primary key (column with unique values) for this table.<br/>
> Each row contains information about the name of a movie, its genre, and its rating.<br/>
> rating is a 2 decimal places float in the range [0, 10]<br/>

Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".

Return the result table ordered by rating in descending order.

The result format is in the following example.

### Example 1:

> Input: <br/>
> Cinema table:<br/>
> +----+------------+-------------+--------+<br/>
> | id | movie      | description | rating |<br/>
> +----+------------+-------------+--------+<br/>
> | 1  | War        | great 3D    | 8.9    |<br/>
> | 2  | Science    | fiction     | 8.5    |<br/>
> | 3  | irish      | boring      | 6.2    |<br/>
> | 4  | Ice song   | Fantacy     | 8.6    |<br/>
> | 5  | House card | Interesting | 9.1    |<br/>
> +----+------------+-------------+--------+<br/>
> Output: <br/>
> +----+------------+-------------+--------+<br/>
> | id | movie      | description | rating |<br/>
> +----+------------+-------------+--------+<br/>
> | 5  | House card | Interesting | 9.1    |<br/>
> | 1  | War        | great 3D    | 8.9    |<br/>
> +----+------------+-------------+--------+<br/>
> Explanation: 
> We have three movies with odd-numbered IDs: 1, 3, and 5. The movie with ID = 3 is boring so we do not include it in the answer.