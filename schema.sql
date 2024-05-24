DROP DATABASE IF EXISTS todo;
CREATE DATABASE todo;

\c  todo;

CREATE TABLE IF NOT EXISTS todolist (
    todo_id INT GENERATED ALWAYS AS IDENTITY,
    item TEXT NOT NULL,
    priority INT NOT NULL DEFAULT 1,
    done BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (todo_id)
);