# AI Chatbot Web App -- Project Context Document

**Generated:** 2026-02-13

------------------------------------------------------------------------

# 1. Project Overview

## Purpose

This project is a public-facing AI chatbot web application.

The chatbot will: - Be trained on a custom knowledge base (uploaded
files / documents) - Answer questions conversationally - Stream
responses in real time - Be open to the public - Have NO traditional
backend (no database, no authentication, no user accounts)

The system must be: - Extremely simple - Blazing fast - Clean
architecture - Easy for an AI coding agent to build and maintain

------------------------------------------------------------------------

# 2. Core Architecture

Although there is "no backend" in the traditional sense, the application
WILL require a minimal serverless API route to securely communicate with
OpenAI.

Architecture flow:

Browser\
→ Serverless API Route\
→ OpenAI API\
→ Streamed response back to browser

No database.\
No login system.\
No user persistence.

------------------------------------------------------------------------

# 3. Tech Stack

## Frontend Framework

-   **Next.js (App Router)**
    -   Built on React
    -   Excellent streaming support
    -   Serverless API routes built-in
    -   Optimized for performance

Alternative (less recommended): - Vite + React (would still require
serverless proxy)

------------------------------------------------------------------------

## Hosting Platform

-   **Vercel**
    -   Native support for Next.js
    -   Global edge network
    -   Easy serverless deployment
    -   Great streaming support

------------------------------------------------------------------------

## Language

-   JavaScript / TypeScript (preferred)

------------------------------------------------------------------------

# 4. OpenAI API Usage

## API Type

Use the modern **OpenAI Responses API**.

Recommended model: - gpt-4.1 (or current recommended general model)

## Streaming

-   Enable streaming (`stream: true`)
-   Use Server-Sent Events (SSE) to stream tokens to frontend
-   Render incremental tokens in chat UI

## Security

-   NEVER expose the OpenAI API key in the browser
-   Store API key as environment variable
-   Use a serverless route as proxy

------------------------------------------------------------------------

# 5. Handling "Trained Data"

Important: The model is NOT traditionally trained.

We will use Retrieval-Augmented Generation (RAG).

------------------------------------------------------------------------

## Recommended Approach: OpenAI File + Vector Store

Steps:

1.  Upload files to OpenAI
2.  Create a Vector Store
3.  Attach files to the Vector Store
4.  On each user query:
    -   The model searches the vector store
    -   Retrieves relevant content
    -   Uses it as context for response generation

Advantages: - No need to manage external vector database - Simple
architecture - Fully managed by OpenAI - Easily updatable knowledge base

------------------------------------------------------------------------

## Not Recommended for This Project

Fine-tuning: - Not suitable for storing large knowledge bases - Better
for behavioral adjustments

------------------------------------------------------------------------

# 6. Application Structure

Single page application.

Homepage contains: - Chat interface - Input field - Streaming message
display - No user accounts - No persistent chat history

Minimal layout: - Header - Chat message window - Input bar

------------------------------------------------------------------------

# 7. Performance Goals

-   Fast initial load
-   Streaming responses
-   Edge-deployed serverless function
-   Lightweight UI
-   No unnecessary dependencies

------------------------------------------------------------------------

# 8. Deployment Flow

1.  Develop using Next.js
2.  Store API key as environment variable
3.  Deploy to Vercel
4.  Serverless API route handles OpenAI calls
5.  Public URL available instantly

------------------------------------------------------------------------

# 9. Design Philosophy

Keep everything: - Simple - Minimal - Maintainable - Scalable -
Public-ready

No overengineering.

------------------------------------------------------------------------

END OF DOCUMENT
