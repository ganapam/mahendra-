{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Copy of Untitled2.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMStkYFI4k2VX2csWbGp4WB",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/ganapam/mahendra-/blob/master/Assignment%201%20_19/06/2020.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pVFcZitVUOb2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XKmHMfF3UTsW",
        "colab_type": "text"
      },
      "source": [
        "1. Write a python program to design simple calculator for the operator"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OYvosD2mVCnZ",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 191
        },
        "outputId": "3b9d5b32-50cd-4ebf-d495-36c33493df70"
      },
      "source": [
        "a=int(input(\"Enter the value of a\")) \n",
        "b=int(input(\"Enter the value of b\")) \n",
        "print(\"sum of two numbers is\", a+b) \n",
        "print(\"Difference of two numbers\", a-b) \n",
        "print(\"product of two numbers is\", a*b) \n",
        "print(\"division of two numbers is\", a/b) \n",
        "print(\"modulus of two numbers is\", a%b) \n",
        "print(\"exponents of two numbers is\", a**b) \n",
        "print(\"floor division is\", a//b)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the value of a2\n",
            "Enter the value of b3\n",
            "sum of two numbers is 5\n",
            "Difference of two numbers -1\n",
            "product of two numbers is 6\n",
            "division of two numbers is 0.6666666666666666\n",
            "modulus of two numbers is 2\n",
            "exponents of two numbers is 8\n",
            "floor division is 0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wyu0qwDbUSFW",
        "colab_type": "text"
      },
      "source": [
        "2. Write a python program to calculate the simple intrest"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MH5y3i_mW3en",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 85
        },
        "outputId": "2f6b745e-5ebc-4684-f0dc-be192b364527"
      },
      "source": [
        "p=int(input(\"Enter the value of p\")) \n",
        "t=int(input(\"Enter the time\")) \n",
        "r=int(input(\"Enter the r\")) \n",
        "print(\"simple intrest is \", (p*t*r) /100) \n",
        "p='principal valley'\n",
        "t='time'\n",
        "r='interest rate'"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the value of p10000\n",
            "Enter the time3\n",
            "Enter the r4\n",
            "simple intrest is  1200.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ERwruskLYIE1",
        "colab_type": "text"
      },
      "source": [
        "3. Write the python program to calculate the area of circle"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LeQZkmr8YaS0",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "e3e3c04d-e538-4bab-db0d-bb40fa6735bc"
      },
      "source": [
        "r=\"radius\"\n",
        "r=int(input(\"Enter the value of r\")) \n",
        "print(\"Area of the circle is\",3.14*r**2)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the value of r3\n",
            "Area of the circle is 28.26\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hNVzwxUUZHjL",
        "colab_type": "text"
      },
      "source": [
        "4. Write the python program to calculate the area of triangle"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2t7HU7FpZSBU",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "cb3d086c-2d61-427a-e2ed-860ddb24ef50"
      },
      "source": [
        "b=\"breadth\"\n",
        "l=\"length\"\n",
        "b=int(input(\"Enter the value of b\")) \n",
        "l=int(input(\"Enter the value of l\")) \n",
        "print(\"Area of triangle is\", 0.5*b*1)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the value of b2\n",
            "Enter the value of l3\n",
            "Area of triangle is 1.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VgM0qEAAZ2qG",
        "colab_type": "text"
      },
      "source": [
        "5. Write a python program to temperature in celslus to fahrenheit"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "n43YIN6EaFTP",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "9cc233f5-bfe5-42cc-f987-9f99d0a5efa7"
      },
      "source": [
        "c=\"celsius temperature\"\n",
        "c=float(input(\"Entre the value of c\")) \n",
        "fahrenheit=(1.8*c+32) \n",
        "print(\"celsius to fahrenheit is\", fahrenheit)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Entre the value of c27.5\n",
            "celsius to fahrenheit is 81.5\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9mACt3lAaver",
        "colab_type": "text"
      },
      "source": [
        "6. Write a python program to calculate the area of rectangle"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "69pSmhUsa6TY",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "c29bb553-691d-4eb3-f972-65548c7eb56e"
      },
      "source": [
        "l=\"length\"\n",
        "b=\"breadth\"\n",
        "l=int(input(\"Enter the value of l\")) \n",
        "b=int(input(\"Enter the value of b\")) \n",
        "print(\"area of rectangle is \", l*b)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the value of l3\n",
            "Enter the value of b2\n",
            "area of rectangle is  6\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-EPFkxZMbh6p",
        "colab_type": "text"
      },
      "source": [
        "7. Write a python program to calculate perimeter of square"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TOqIaf1MbyBU",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "2f19a009-a83f-45c9-ff9d-ba389d9e129a"
      },
      "source": [
        "a=\"side of square \"\n",
        "a=int(input(\"Enter the value of a\")) \n",
        "print(\"perimeter of square is\", 4*a)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the value of a2\n",
            "perimeter of square is 8\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wNNvDf-GcPir",
        "colab_type": "text"
      },
      "source": [
        "8. Write a python program to calculate circumference of a circle"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4_xnt0RPcdS6",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "e556b909-ab28-455a-e09e-645132926e91"
      },
      "source": [
        "r=\"radius of circle \"\n",
        "r=int(input(\"Enter the value of r\")) \n",
        "print(\"circumference of circle is\", 2*1.14*r)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the value of r4\n",
            "circumference of circle is 9.12\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QCbpfnGIdQ8q",
        "colab_type": "text"
      },
      "source": [
        "9.write a python program to swap two numbers"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WzYbwuhCdZXu",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 85
        },
        "outputId": "d9a0c280-2daf-462e-fca1-9f9f7bdde683"
      },
      "source": [
        "x=int(input(\"Enter the value of x\")) \n",
        "y=int(input(\"Enter the value of y\"))\n",
        "temp='x'\n",
        "x='y'\n",
        "y='temp'\n",
        "print(\"the value of x after swaping\") \n",
        "print(\"the value of y after swaping\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the value of x3\n",
            "Enter the value of y4\n",
            "the value of x after swaping\n",
            "the value of y after swaping\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}