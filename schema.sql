DROP DATABASE IF EXISTS todo;
CREATE DATABASE todo;

\c  todo;

CREATE TABLE IF NOT EXISTS todolist (
    todo_id INT GENERATED ALWAYS AS IDENTITY,
    item TEXT NOT NULL,
    priority INT NOT NULL DEFAULT 1,
    PRIMARY KEY (todo_id)
);

CREATE TABLE IF NOT EXISTS completed (
    completed_id INT GENERATED ALWAYS AS IDENTITY,
    item TEXT NOT NULL,
    PRIMARY KEY (completed_id)
);