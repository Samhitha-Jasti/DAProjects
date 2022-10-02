{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPxqN6RoIx3px2Fi1iwI3qb",
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
        "<a href=\"https://colab.research.google.com/github/Samhitha-Jasti/DAProjects/blob/BabyNameAnalysis/BabyNameAnalysis.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "LeaexEHLrSkg"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "urlfile=\"https://raw.githubusercontent.com/PhantomInsights/baby-names-analysis/master/data/data.csv\"\n",
        "babynames=pd.read_csv(urlfile)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "babynames"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "nmpc7-y9r5JQ",
        "outputId": "ef122b03-0cac-4d9c-d6b0-40cf20c1b300"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         year       name gender  count\n",
              "0        1880       Mary      F   7065\n",
              "1        1880       Anna      F   2604\n",
              "2        1880       Emma      F   2003\n",
              "3        1880  Elizabeth      F   1939\n",
              "4        1880     Minnie      F   1746\n",
              "...       ...        ...    ...    ...\n",
              "2020342  2020     Zykell      M      5\n",
              "2020343  2020      Zylus      M      5\n",
              "2020344  2020     Zymari      M      5\n",
              "2020345  2020        Zyn      M      5\n",
              "2020346  2020      Zyran      M      5\n",
              "\n",
              "[2020347 rows x 4 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-8c3a5790-ac1b-4745-88e9-a841cb403d81\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>year</th>\n",
              "      <th>name</th>\n",
              "      <th>gender</th>\n",
              "      <th>count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1880</td>\n",
              "      <td>Mary</td>\n",
              "      <td>F</td>\n",
              "      <td>7065</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1880</td>\n",
              "      <td>Anna</td>\n",
              "      <td>F</td>\n",
              "      <td>2604</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1880</td>\n",
              "      <td>Emma</td>\n",
              "      <td>F</td>\n",
              "      <td>2003</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1880</td>\n",
              "      <td>Elizabeth</td>\n",
              "      <td>F</td>\n",
              "      <td>1939</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1880</td>\n",
              "      <td>Minnie</td>\n",
              "      <td>F</td>\n",
              "      <td>1746</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020342</th>\n",
              "      <td>2020</td>\n",
              "      <td>Zykell</td>\n",
              "      <td>M</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020343</th>\n",
              "      <td>2020</td>\n",
              "      <td>Zylus</td>\n",
              "      <td>M</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020344</th>\n",
              "      <td>2020</td>\n",
              "      <td>Zymari</td>\n",
              "      <td>M</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020345</th>\n",
              "      <td>2020</td>\n",
              "      <td>Zyn</td>\n",
              "      <td>M</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020346</th>\n",
              "      <td>2020</td>\n",
              "      <td>Zyran</td>\n",
              "      <td>M</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>2020347 rows × 4 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-8c3a5790-ac1b-4745-88e9-a841cb403d81')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-8c3a5790-ac1b-4745-88e9-a841cb403d81 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-8c3a5790-ac1b-4745-88e9-a841cb403d81');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "babynames.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "xqq_yUYAr6zp",
        "outputId": "dcb7166e-b30b-4284-bdf6-09676ffce10d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   year       name gender  count\n",
              "0  1880       Mary      F   7065\n",
              "1  1880       Anna      F   2604\n",
              "2  1880       Emma      F   2003\n",
              "3  1880  Elizabeth      F   1939\n",
              "4  1880     Minnie      F   1746"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-75fead6c-0823-4d64-82bd-a3f66540db13\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>year</th>\n",
              "      <th>name</th>\n",
              "      <th>gender</th>\n",
              "      <th>count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1880</td>\n",
              "      <td>Mary</td>\n",
              "      <td>F</td>\n",
              "      <td>7065</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1880</td>\n",
              "      <td>Anna</td>\n",
              "      <td>F</td>\n",
              "      <td>2604</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1880</td>\n",
              "      <td>Emma</td>\n",
              "      <td>F</td>\n",
              "      <td>2003</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1880</td>\n",
              "      <td>Elizabeth</td>\n",
              "      <td>F</td>\n",
              "      <td>1939</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1880</td>\n",
              "      <td>Minnie</td>\n",
              "      <td>F</td>\n",
              "      <td>1746</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-75fead6c-0823-4d64-82bd-a3f66540db13')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-75fead6c-0823-4d64-82bd-a3f66540db13 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-75fead6c-0823-4d64-82bd-a3f66540db13');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
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
        "babynames.tail()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "0MfzGW4jKw7r",
        "outputId": "31c4babc-8de6-4db6-fbeb-e3a13e547930"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         year    name gender  count\n",
              "2020342  2020  Zykell      M      5\n",
              "2020343  2020   Zylus      M      5\n",
              "2020344  2020  Zymari      M      5\n",
              "2020345  2020     Zyn      M      5\n",
              "2020346  2020   Zyran      M      5"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-2d2630c2-e4b9-42ff-98f7-873fe3c75252\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>year</th>\n",
              "      <th>name</th>\n",
              "      <th>gender</th>\n",
              "      <th>count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2020342</th>\n",
              "      <td>2020</td>\n",
              "      <td>Zykell</td>\n",
              "      <td>M</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020343</th>\n",
              "      <td>2020</td>\n",
              "      <td>Zylus</td>\n",
              "      <td>M</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020344</th>\n",
              "      <td>2020</td>\n",
              "      <td>Zymari</td>\n",
              "      <td>M</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020345</th>\n",
              "      <td>2020</td>\n",
              "      <td>Zyn</td>\n",
              "      <td>M</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020346</th>\n",
              "      <td>2020</td>\n",
              "      <td>Zyran</td>\n",
              "      <td>M</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-2d2630c2-e4b9-42ff-98f7-873fe3c75252')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-2d2630c2-e4b9-42ff-98f7-873fe3c75252 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-2d2630c2-e4b9-42ff-98f7-873fe3c75252');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "babynames.gender.unique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Kvbkq2fSLSEH",
        "outputId": "0fd0ff8f-b2de-41a1-acd4-7d56da6e8c23"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['F', 'M'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Sorting DataFrame by alphabetical order of names"
      ],
      "metadata": {
        "id": "0ChrV4_lK17Z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "babynames2=babynames.sort_values('name')\n",
        "babynames2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "zntGDK69Kj7N",
        "outputId": "83f37c1e-0029-4aa7-fefc-91053b177229"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         year     name gender  count\n",
              "1886382  2016    Aaban      M      9\n",
              "1752571  2012    Aaban      M     11\n",
              "1685983  2010    Aaban      M      9\n",
              "1718670  2011    Aaban      M     11\n",
              "1586216  2007    Aaban      M      5\n",
              "...       ...      ...    ...    ...\n",
              "1856007  2015    Zyvon      M      7\n",
              "1675008  2010  Zyyanna      F      6\n",
              "1824324  2014    Zyyon      M      6\n",
              "1692111  2010    Zzyzx      M      5\n",
              "1957045  2018    Zzyzx      M      5\n",
              "\n",
              "[2020347 rows x 4 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-66241ac9-f72b-45bf-8f91-e62dc378c2b8\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>year</th>\n",
              "      <th>name</th>\n",
              "      <th>gender</th>\n",
              "      <th>count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1886382</th>\n",
              "      <td>2016</td>\n",
              "      <td>Aaban</td>\n",
              "      <td>M</td>\n",
              "      <td>9</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1752571</th>\n",
              "      <td>2012</td>\n",
              "      <td>Aaban</td>\n",
              "      <td>M</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1685983</th>\n",
              "      <td>2010</td>\n",
              "      <td>Aaban</td>\n",
              "      <td>M</td>\n",
              "      <td>9</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1718670</th>\n",
              "      <td>2011</td>\n",
              "      <td>Aaban</td>\n",
              "      <td>M</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1586216</th>\n",
              "      <td>2007</td>\n",
              "      <td>Aaban</td>\n",
              "      <td>M</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1856007</th>\n",
              "      <td>2015</td>\n",
              "      <td>Zyvon</td>\n",
              "      <td>M</td>\n",
              "      <td>7</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1675008</th>\n",
              "      <td>2010</td>\n",
              "      <td>Zyyanna</td>\n",
              "      <td>F</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1824324</th>\n",
              "      <td>2014</td>\n",
              "      <td>Zyyon</td>\n",
              "      <td>M</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1692111</th>\n",
              "      <td>2010</td>\n",
              "      <td>Zzyzx</td>\n",
              "      <td>M</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1957045</th>\n",
              "      <td>2018</td>\n",
              "      <td>Zzyzx</td>\n",
              "      <td>M</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>2020347 rows × 4 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-66241ac9-f72b-45bf-8f91-e62dc378c2b8')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-66241ac9-f72b-45bf-8f91-e62dc378c2b8 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-66241ac9-f72b-45bf-8f91-e62dc378c2b8');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Number of Unique Male Names in data frame"
      ],
      "metadata": {
        "id": "8eLHW034MXLY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#babynames[babynames[\"gender\"==\"M\"]].sum()\n",
        "babynames[babynames[\"gender\"] == \"M\"][\"name\"].nunique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xkB2yGHeKyTP",
        "outputId": "919c2fe7-190c-43ff-906c-72c3976916b2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "42555"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Number of Unique Female Names in data frame"
      ],
      "metadata": {
        "id": "Oj0vBQdiMeav"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "babynames[babynames[\"gender\"] == \"F\"][\"name\"].nunique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UNYreniZMP9i",
        "outputId": "0b8d170e-f79f-4d48-9446-b06976364ae9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "68883"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Top 20 Gender Neutral Names"
      ],
      "metadata": {
        "id": "979YBIy0JbCY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "babynames.pivot_table(index=\"name\", columns=\"gender\", values=\"count\", aggfunc=np.sum).dropna()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 455
        },
        "id": "FiJjHatIJI9K",
        "outputId": "08adc4d2-58a1-4180-aa7d-5ce5b739f752"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "gender         F       M\n",
              "name                    \n",
              "Aaden        5.0  4975.0\n",
              "Aadi        16.0   933.0\n",
              "Aadyn       16.0   555.0\n",
              "Aalijah    149.0   243.0\n",
              "Aaliyah  94641.0   101.0\n",
              "...          ...     ...\n",
              "Zyion      186.0  1068.0\n",
              "Zyon       661.0  3024.0\n",
              "Zyonn        5.0    59.0\n",
              "Zyree       16.0   116.0\n",
              "Zyrie       26.0    33.0\n",
              "\n",
              "[11103 rows x 2 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-aea3c49c-e28a-4fc6-99d2-9245fa6baa3f\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th>gender</th>\n",
              "      <th>F</th>\n",
              "      <th>M</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>name</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Aaden</th>\n",
              "      <td>5.0</td>\n",
              "      <td>4975.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aadi</th>\n",
              "      <td>16.0</td>\n",
              "      <td>933.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aadyn</th>\n",
              "      <td>16.0</td>\n",
              "      <td>555.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aalijah</th>\n",
              "      <td>149.0</td>\n",
              "      <td>243.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Aaliyah</th>\n",
              "      <td>94641.0</td>\n",
              "      <td>101.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Zyion</th>\n",
              "      <td>186.0</td>\n",
              "      <td>1068.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Zyon</th>\n",
              "      <td>661.0</td>\n",
              "      <td>3024.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Zyonn</th>\n",
              "      <td>5.0</td>\n",
              "      <td>59.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Zyree</th>\n",
              "      <td>16.0</td>\n",
              "      <td>116.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Zyrie</th>\n",
              "      <td>26.0</td>\n",
              "      <td>33.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>11103 rows × 2 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-aea3c49c-e28a-4fc6-99d2-9245fa6baa3f')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-aea3c49c-e28a-4fc6-99d2-9245fa6baa3f button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-aea3c49c-e28a-4fc6-99d2-9245fa6baa3f');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Percentage of Female Names Vs Male Names"
      ],
      "metadata": {
        "id": "kIUahltwRAZv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "babynames.groupby('gender').agg({\n",
        "    'count':'sum'\n",
        "}) / babynames['count'].sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "id": "FFuMYmqtMQLw",
        "outputId": "a42d63c0-13cc-4fa5-fe9f-c74efa445d20"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "           count\n",
              "gender          \n",
              "F       0.494814\n",
              "M       0.505186"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-dc6deab4-a239-4dab-8c20-100f0326804c\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>count</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>gender</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>F</th>\n",
              "      <td>0.494814</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>M</th>\n",
              "      <td>0.505186</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-dc6deab4-a239-4dab-8c20-100f0326804c')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-dc6deab4-a239-4dab-8c20-100f0326804c button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-dc6deab4-a239-4dab-8c20-100f0326804c');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Grouping the Data set by Names"
      ],
      "metadata": {
        "id": "J-YHOWFsRkXH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "names=babynames.groupby('name')\n",
        "names"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lfejU6IOQbao",
        "outputId": "0d513e1d-346b-4796-c6d6-a62916e4d995"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f68d9352410>"
            ]
          },
          "metadata": {},
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "babynames.groupby('gender')['count'].sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZN4TaM5JWbLc",
        "outputId": "8ae59648-63d9-4d1c-e77e-5eaa84cb33a9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "gender\n",
              "F    177348487\n",
              "M    181065743\n",
              "Name: count, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "TcMLIuLhWrTc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Number of Unique Names"
      ],
      "metadata": {
        "id": "Q9FyuSEbT_qW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "babynames['name'].nunique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AfiCiTE7UIyp",
        "outputId": "0abc04f9-622a-405e-caf0-099609de1cf5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "100335"
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Most Occurred Name"
      ],
      "metadata": {
        "id": "VmkT5-5rUTkz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "names['count'].sum().sort_values(ascending=False)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P6iuRa69Urcb",
        "outputId": "9143c866-5c40-4d52-f678-6521d18496a3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "name\n",
              "James        5213191\n",
              "John         5163524\n",
              "Robert       4849409\n",
              "Michael      4404794\n",
              "William      4159492\n",
              "              ...   \n",
              "Kudrat             5\n",
              "Kubrick            5\n",
              "Kubo               5\n",
              "Thornwell          5\n",
              "Nicho              5\n",
              "Name: count, Length: 100335, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Gender Neutral Count According to Birth Year"
      ],
      "metadata": {
        "id": "gZwMC6KoOPP3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "birth_year=babynames.groupby('year')['year'].count()\n",
        "birth_year"
      ],
      "metadata": {
        "id": "QuMIZ7XxYdVW",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "299d3835-6701-4091-8c2e-aa87dcdca47b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "year\n",
              "1880     2000\n",
              "1881     1935\n",
              "1882     2127\n",
              "1883     2084\n",
              "1884     2297\n",
              "        ...  \n",
              "2016    33010\n",
              "2017    32590\n",
              "2018    32033\n",
              "2019    32030\n",
              "2020    31271\n",
              "Name: year, Length: 141, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Female and Male Names count according to Birth Year"
      ],
      "metadata": {
        "id": "WvrRx5bUOWGp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "birth_year=babynames.groupby(['year','gender'])['year'].count()\n",
        "birth_year"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HL-gLETxOCsG",
        "outputId": "9629fc64-a20a-45a0-abd6-977f1c8c14ad"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "year  gender\n",
              "1880  F           942\n",
              "      M          1058\n",
              "1881  F           938\n",
              "      M           997\n",
              "1882  F          1028\n",
              "                ...  \n",
              "2018  M         14004\n",
              "2019  F         17948\n",
              "      M         14082\n",
              "2020  F         17360\n",
              "      M         13911\n",
              "Name: year, Length: 282, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "birth_year.plot(title=\"Total Names by gender and year\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 313
        },
        "id": "VaDrCuU8Rnmb",
        "outputId": "6ea13fc2-de26-4dd1-90a0-019146197562"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f9a0bdf7990>"
            ]
          },
          "metadata": {},
          "execution_count": 14
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Female and Male Population Count according to Birth year"
      ],
      "metadata": {
        "id": "8uFWRqDpQYLq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "total_births=babynames.pivot_table('count',index='year',columns='gender',aggfunc=sum)\n",
        "total_births"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 455
        },
        "id": "2YzD68-pQEhL",
        "outputId": "0399e0e5-909f-4790-93b4-8c7f3d1ab6c5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "gender        F        M\n",
              "year                    \n",
              "1880      90994   110490\n",
              "1881      91953   100743\n",
              "1882     107847   113686\n",
              "1883     112319   104625\n",
              "1884     129019   114442\n",
              "...         ...      ...\n",
              "2016    1766212  1891585\n",
              "2017    1719138  1842837\n",
              "2018    1686961  1800392\n",
              "2019    1670419  1785527\n",
              "2020    1598836  1706423\n",
              "\n",
              "[141 rows x 2 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-d998f1d5-b69c-46a0-af57-a965e919621f\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th>gender</th>\n",
              "      <th>F</th>\n",
              "      <th>M</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>year</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1880</th>\n",
              "      <td>90994</td>\n",
              "      <td>110490</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1881</th>\n",
              "      <td>91953</td>\n",
              "      <td>100743</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1882</th>\n",
              "      <td>107847</td>\n",
              "      <td>113686</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1883</th>\n",
              "      <td>112319</td>\n",
              "      <td>104625</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1884</th>\n",
              "      <td>129019</td>\n",
              "      <td>114442</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2016</th>\n",
              "      <td>1766212</td>\n",
              "      <td>1891585</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2017</th>\n",
              "      <td>1719138</td>\n",
              "      <td>1842837</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2018</th>\n",
              "      <td>1686961</td>\n",
              "      <td>1800392</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019</th>\n",
              "      <td>1670419</td>\n",
              "      <td>1785527</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020</th>\n",
              "      <td>1598836</td>\n",
              "      <td>1706423</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>141 rows × 2 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-d998f1d5-b69c-46a0-af57-a965e919621f')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-d998f1d5-b69c-46a0-af57-a965e919621f button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-d998f1d5-b69c-46a0-af57-a965e919621f');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "total_births.plot(title=\"Total births by gender and year\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 313
        },
        "id": "yCMFdb8IRfow",
        "outputId": "d86d3034-b39e-4873-e59e-eeedc649233f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f9a0c474990>"
            ]
          },
          "metadata": {},
          "execution_count": 13
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "cKiJ7Q_oRk1u"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
