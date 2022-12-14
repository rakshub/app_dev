{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMuMdYb5peQ17vfAGwAeFNM",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rakshub/app_dev/blob/main/heroku_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9luCGbA5LRJH",
        "outputId": "8f5896be-ec73-44b9-afd4-12621b62a3ae"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[K     |████████████████████████████████| 10.3 MB 8.4 MB/s \n",
            "\u001b[K     |████████████████████████████████| 4.7 MB 43.3 MB/s \n",
            "\u001b[K     |████████████████████████████████| 182 kB 60.3 MB/s \n",
            "\u001b[K     |████████████████████████████████| 164 kB 69.0 MB/s \n",
            "\u001b[K     |████████████████████████████████| 237 kB 55.6 MB/s \n",
            "\u001b[K     |████████████████████████████████| 78 kB 7.6 MB/s \n",
            "\u001b[K     |████████████████████████████████| 62 kB 1.2 MB/s \n",
            "\u001b[K     |████████████████████████████████| 51 kB 6.5 MB/s \n",
            "\u001b[?25h  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n"
          ]
        }
      ],
      "source": [
        "!pip install -q streamlit\n",
        "import streamlit as st"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "st.write(\"Two integer subtraction\")"
      ],
      "metadata": {
        "id": "m1SUsw76PZaB"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.header(\"Subtraction Program\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LMw0C25kPx5J",
        "outputId": "1d8e92a4-d5f3-4584-a878-5d4f91202840"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def user_input(): \n",
        "  st.title(\"Subtraction\")\n",
        "  html_temp=\"\"\"\n",
        "  <div style=\"background-color:black;padding:10x\">\n",
        "  <h style=\"color:white;text-align:center:\">Subtraction of 2 numbers using streamlit</h2>\n",
        "  </div>\"\"\"\n",
        "  st.markdown(html_temp,unsafe_allow_html=True)\n",
        "  input1=st.number_input(\"Give first integer:\")\n",
        "  input2=st.number_input(\"Give second integer:\")\n",
        "  answer=input1-input2\n",
        "  st.success(\"The output is {}\".format(answer))\n",
        "  st.write(\"CREDIT:21f1003674\")\n"
      ],
      "metadata": {
        "id": "CWA5oCOPPgnw"
      },
      "execution_count": 12,
      "outputs": []
    }
  ]
}