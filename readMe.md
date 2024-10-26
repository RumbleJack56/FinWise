# FinWise

## Project Description
**FinWise** is a dashboard service that provides easy access to trading infographics, details, and advice. Utilizing **Retrieval-Augmented Generation (RAG)** and **Large Language Models (LLMs)**, FinWise delivers comprehensive financial insights and sound advice, empowering traders—especially beginners and casual users—to make informed decisions.

## Target Problem
Many beginners and casual traders lack access to real-time data, effective tools, and educational resources, leading to uninformed trading decisions.

## Key Features
- **Retrieval-Augmented Generation (RAG):** Real-time financial insights by retrieving market data.
- **Chatbot Integration:** Provides guidance, answers questions, and offers insights through a voice-enabled chatbot.
- **Risk Management Tools:** Helps traders manage risks effectively.
- **Portfolio Tracking and Analysis:** Allows users to monitor their investments and identify opportunities.
- **Dashboards:** Displays stock performance and trends for easy navigation.
- **Upstox API Integration:** Real-time data and trade management.
- **Customizable Alerts:** Keeps users informed of important market shifts.
- **Secure Sign-In:** Authentication via Supabase for secure access to portfolios.

  ## Instructions on How OnDemand APIs Are Utilized in Your Project
**Integration with OnDemand:** FinWise utilizes OnDemand APIs to provide real-time financial insights. The APIs are used for:
- **Market Data Retrieval:** Pulling live stock data to ensure users have the most up-to-date information.
- **AI-Enhanced Financial Advice:** Leveraging OnDemand’s algorithms to offer personalized trading recommendations based on current market conditions.
- **Dynamic Tracking:** Allowing users to manage their portfolios with real-time updates via OnDemand’s extensive data capabilities.


## Installation and Setup Instructions
To set up FinWise on your local machine, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/finwise.git
    cd finwise
    ```

2. **Install dependencies:**

    Ensure you have Node.js installed. Then run:

    ```bash
    npm install
    ```

    or using Yarn:

    ```bash
    yarn install
    ```

3. **Set up environment variables:**

    Create a `.env.local` file in the root directory and include your environment variables:

    ```env
    DATABASE_URL=your_database_url
    API_KEY=your_api_key
    SUPABASE_URL=your_supabase_url
    UPSTOX_API_KEY=your_upstox_api_key
    ```

4. **Run the application:**

    Start the development server:

    ```bash
    npm run dev
    ```

    or

    ```bash
    yarn dev
    ```

    Open your browser and navigate to `http://localhost:3000` to access the application.

## Usage Guidelines
- **Sign In:** Users can log in by clicking the "Sign in" button. New users can create an account by selecting "Get started."
- **Dashboard:** Once logged in, users will see their dashboard with key metrics and chatbot access.
- **Chatbot Functionality:** Use the voice-enabled chatbot for real-time financial guidance.
- **Portfolio Tracking:** Add stocks and manage investments in real-time.
- **Alerts and Insights:** Configure alerts for significant market changes and receive personalized insights.

### Challenges Faced
- Managing intermittent data requests and ensuring seamless communication between services.
- Standardizing API response formats to avoid parsing errors and improve reliability.
- Implementing caching mechanisms to manage API requests efficiently and reduce latency.

## Team Member Names and Roles
- **Ved Mohan:** Frontend Development and Design
- **Ujjwal Kakar:** AI Operations & On-Demand Organization
- **Pragya Singh:** Backend & API Development
- **Aditi Parnaik:** Frontend Development & Workflow Design
