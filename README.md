# 💊 Drug Sales Forecasting with ARIMA

A simple yet powerful ARIMA-based Time Series Forecasting app built using Streamlit.  
Upload your dataset, select how many months you want to forecast, and visualize it instantly.

🔗 **Live Demo**: [Drug Sales Forecasting App](https://drugsalesforecasting.streamlit.app/)  
📂 **GitHub Repo**: [Drug Sales Forecasting](https://github.com/Verma-Rohil/Drug_Sales_Forecasting)

![Time Series Forecasting](https://media.geeksforgeeks.org/wp-content/uploads/20230519175413/Time-Series-Forecasting.webp)

---

## 🚀 Features

- 📄 Upload monthly sales dataset (`dataset.txt`)  
- 🔍 Visualize historical data vs. forecasted values  
- ⚙️ Adjustable forecast horizon using slider  
- 📈 Confidence interval shading for uncertainty  
- 🎯 Powered by ARIMA (`pmdarima`) modeling  
- 🧠 Loads pre-trained model with `joblib`  

---


## 🧩 Project Structure

```
.
├── arima_model.pkl # Trained ARIMA model
├── dataset.txt # Sample drug sales data
├── app.py # Streamlit frontend and logic
├── requirements.txt # Python dependencies
└── README.md # Project overview (this file)
```


---

## 🧠 Tech Stack

| Layer        | Technology          |
|-------------|---------------------|
| UI          | Streamlit           |
| Forecasting | ARIMA (pmdarima)    |
| Model Store | joblib              |
| Plotting    | Matplotlib          |
| Data        | Pandas              |

---

## ⚙️ How It Works

1. **Load ARIMA model** trained on drug sales time series  
2. **Choose forecast horizon** from sidebar slider  
3. **Generate forecast + confidence bounds**
4. **Plot results** with shaded uncertainty
5. **View and download forecasted table**

---


---



## ☁️ Deployment

### 🔹 Streamlit Cloud

1. Push this repo to GitHub  
2. Connect your repo to [Streamlit Cloud](https://streamlit.io/cloud)  
3. Add your `GOOGLE_API_KEY` (or other required keys) in **Secrets** via `Settings → Secrets`  

### 🔹 GCP / Cloud Run (Advanced)

- Use the provided `Dockerfile` and GitHub Actions for CI/CD  
- Automatically deploy to GCP from GitHub  
- Need help setting this up? Just ask!

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, share, and modify it for educational or commercial purposes.

✨ Made by [Rohil Verma](https://www.linkedin.com/in/verma-rohil/) with ❤️

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!  
Feel free to fork the repository, create a feature branch, and open a pull request.

If you find a bug or want to suggest a new feature:  
- Open an [issue](https://github.com/Verma-Rohil/Drug_Sales_Forecasting/issues)  
- Or reach out directly via [LinkedIn](https://www.linkedin.com/in/verma-rohil/)

---

## 💡 Future Improvements

Here are some potential next steps to enhance the forecasting application:

- [ ] 🧠 Integrate additional forecasting models (SARIMA, Prophet, LSTM) for better accuracy and comparison  
- [ ] 📊 Add interactive and zoomable visualizations using Plotly or Altair  
- [ ] 📈 Support multivariate forecasting by including external regressors (e.g., holidays, promotions)  
- [ ] 🔍 Improve model diagnostics and explainability (residual analysis, SHAP, prediction intervals)  
- [ ] 📦 Enable scheduled forecast exports in CSV or PDF formats  
- [ ] ☁️ Containerize the app using Docker for scalable cloud deployment  
- [ ] 🔐 Implement role-based access and session-based user data for a multi-user experience  

---

## 📌 Related Resources

- [Streamlit Docs](https://docs.streamlit.io/)  
- [scikit-learn](https://scikit-learn.org/)  
- [pmdarima (ARIMA models)](https://alkaline-ml.com/pmdarima/)  
- [statsmodels](https://www.statsmodels.org/)  
- [GitHub Actions](https://docs.github.com/en/actions)

