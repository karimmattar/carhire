CREATE TABLE vehicle_category
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    name         VARCHAR(50) NOT NULL,
    max_capacity INT         NOT NULL
);

CREATE TABLE vehicle
(
    id            INT PRIMARY KEY AUTO_INCREMENT,
    category_id   INT          NOT NULL,
    description   VARCHAR(255) NOT NULL,
    color         VARCHAR(50)  NOT NULL,
    brand         VARCHAR(50)  NOT NULL,
    model         VARCHAR(50)  NOT NULL,
    purchase_date DATE         NOT NULL,
    available     BOOLEAN      NOT NULL DEFAULT true,
    FOREIGN KEY (category_id) REFERENCES vehicle_category (id)
);

CREATE TABLE customer
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    ssn          VARCHAR(20)  NOT NULL,
    first_name   VARCHAR(50)  NOT NULL,
    last_name    VARCHAR(50)  NOT NULL,
    email        VARCHAR(255) NOT NULL UNIQUE,
    mobile_phone VARCHAR(20)  NOT NULL,
    status       VARCHAR(50)  NOT NULL,
    country      VARCHAR(50)  NOT NULL,
    password     VARCHAR(512) NOT NULL
);

CREATE TABLE booking
(
    id          INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT            NOT NULL,
    vehicle_id  INT            NOT NULL,
    pickup_date DATE           NOT NULL,
    return_date DATE           NOT NULL,
    amount      DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer (id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicle (id),
    CONSTRAINT max_duration CHECK (DATEDIFF(return_date, pickup_date) <= 7)
);

CREATE TABLE invoice
(
    id         INT PRIMARY KEY AUTO_INCREMENT,
    booking_id INT            NOT NULL,
    amount     DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (booking_id) REFERENCES booking (id)
);