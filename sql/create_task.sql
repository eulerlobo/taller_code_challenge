CREATE TABLE task (
    id SERIAL PRIMARY KEY,
    project_id BIGINT NOT NULL,
    title VARCHAR(255) NOT NULL,
    priority INTEGER,
    completed BOOLEAN DEFAULT FALSE,
    due_date DATE,
    CONSTRAINT fk_project
        FOREIGN KEY(project_id)
        REFERENCES project(id)
);

-- INDEX to optimize queries filtering by project_id and priority
CREATE INDEX idx_task_project_priority ON task(project_id, priority);