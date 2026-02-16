# Basics of HTTP/HTTPS  
## Technical Documentation  

---

## 1. Introduction  

### 1.1 Purpose of This Document  

This document explains the fundamental concepts of HTTP and HTTPS.  

Its purpose is to clarify how web communication works, how data is transferred between client and server, and how security is ensured through HTTPS.  

This document covers:  

- Differences between HTTP and HTTPS  
- Structure of HTTP requests and responses  
- Common HTTP methods  
- Common HTTP status codes  

---

## 2. Difference Between HTTP and HTTPS  

### 2.1 HTTP Overview  

HTTP (Hypertext Transfer Protocol) is the protocol used for communication between web clients and web servers.  

It allows clients (such as browsers or applications) to request resources like HTML pages, images, or API data.  

HTTP operates in plaintext, meaning that data is not encrypted during transmission.  

---

### 2.2 HTTPS Overview  

HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP.  

It uses SSL/TLS encryption to protect data exchanged between the client and the server.  

This encryption ensures:  

- Confidentiality  
- Integrity  
- Authentication  

---

### 2.3 Key Differences  

- HTTP does not encrypt data.  
- HTTPS encrypts all transmitted data.  
- HTTP uses port **80** by default.  
- HTTPS uses port **443** by default.  
- HTTPS requires a valid SSL/TLS certificate.  

HTTPS is mandatory for applications handling sensitive information such as passwords, banking data, or personal information.  

---

## 3. Structure of HTTP Communication  

### 3.1 HTTP Request Structure  

An HTTP request is composed of three main parts:  

#### 1. Request Line  

Contains:  

- HTTP Method  
- Resource path (URL)  
- HTTP version  

Example:

```
GET /index.html HTTP/1.1
```

#### 2. Headers  

Provide additional metadata about the request.  

Common headers include:  

- Host  
- User-Agent  
- Content-Type  
- Authorization  

#### 3. Body (Optional)  

Contains data sent to the server.  

Typically used with:  

- POST  
- PUT  

---

### 3.2 HTTP Response Structure  

An HTTP response also contains three main parts:  

#### 1. Status Line  

Contains:  

- HTTP version  
- Status code  
- Status message  

Example:

```
HTTP/1.1 200 OK
```

#### 2. Headers  

Provide metadata about the response.  

Common headers include:  

- Content-Type  
- Content-Length  
- Set-Cookie  

#### 3. Body  

Contains the requested resource:  

- HTML page  
- JSON data  
- Image  
- File  

---

## 4. Common HTTP Methods  

### 4.1 GET  

Description: Retrieves data from the server.  
Use Case: Fetching a web page or retrieving API data.  

### 4.2 POST  

Description: Sends data to the server to create a new resource.  
Use Case: Submitting a form or creating a user account.  

### 4.3 PUT  

Description: Updates an existing resource.  
Use Case: Modifying user information.  

### 4.4 DELETE  

Description: Removes a resource from the server.  
Use Case: Deleting a record from a database.  

---

## 5. Common HTTP Status Codes  

### 5.1 200 OK  

Meaning: The request was successful.  
Scenario: A webpage loads correctly.  

### 5.2 201 Created  

Meaning: A resource was successfully created.  
Scenario: A new user account is created.  

### 5.3 400 Bad Request  

Meaning: The request is invalid or malformed.  
Scenario: Required fields are missing.  

### 5.4 404 Not Found  

Meaning: The requested resource does not exist.  
Scenario: Accessing a deleted or nonexistent page.  

### 5.5 500 Internal Server Error  

Meaning: The server encountered an unexpected error.  
Scenario: A backend exception occurs.  

---

## 6. Conclusion  

This document explains the foundations of HTTP and HTTPS.  

It defines:  

- The security differences between HTTP and HTTPS  
- The structure of HTTP requests and responses  
- The most commonly used HTTP methods  
- The most frequent HTTP status codes  

Understanding these concepts is essential for API development, web communication, and secure system design.  