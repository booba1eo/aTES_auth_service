-- upgrade --
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TYPE users__role_enum AS ENUM ('admin', 'manager', 'employee');

CREATE TABLE IF NOT EXISTS "users" (
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ,
    "id" SERIAL NOT NULL PRIMARY KEY,
    "public_id" UUID NOT NULL UNIQUE  DEFAULT uuid_generate_v4(),
    "full_name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(120) NOT NULL UNIQUE,
    "password" VARCHAR(128) NOT NULL,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "position" VARCHAR(255) NOT NULL,
    "role" users__role_enum NOT NULL
);

COMMENT ON COLUMN "users"."role" IS 'User role';

-- downgrade --
DROP TABLE IF EXISTS "users";
