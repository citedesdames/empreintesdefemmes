#!/usr/sfw/bin/python
# -*- coding: utf-8 -*-

import os, re, sys, time, requests, shutil

# pip3 install selenium
# install "geckodriver" from https://github.com/mozilla/geckodriver/releases
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

driver = webdriver.Firefox()

images = [
"http://commons.wikimedia.org/wiki/Special:FilePath/Morisot%20berthe%20photo.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Sonia%20Delaunay%20portrait%20photograph.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Tacita%20Dean%2C%202011%20-%20detail.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Suzanne%20Valadon.%20Portrait%20au%20chapeau%2C%20photographie%2C%20vers%201885.%20Ville%20de%20Paris%20Biblioth%C3%A8que%20Marguerite%20Durand%20%28BMD%29.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Marie%20Curie%20c.%201920s.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Germain.jpeg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Beguine%201489.png",
"http://commons.wikimedia.org/wiki/Special:FilePath/Marion%20Tournon-Branly%20%28cropped%29.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Alice%20Guy.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Louise%20Farrenc.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Marion%20Tournon-Branly%20%28cropped%29.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Charlotte%20Perriand%20Janvier%201991.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Mlle%20Montansier%201790%20-%20Londr%C3%A9%201991%20p186.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Aulenti02.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/MJ%20Carpentier.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Clotilde%20de%20Vaux%20%28maison%20d%27A.%20Comte%2C%20Paris%29.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Andr%C3%A9%20Adolphe-Eug%C3%A8ne%20Disd%C3%A9ri%20%28French%20-%20%28Rosa%20Bonheur%29%20-%20Google%20Art%20Project.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Valerie%20Simonin%20portrait.png",
"http://commons.wikimedia.org/wiki/Special:FilePath/Eileen%20Gray.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Marie-de-Gournay-2.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Marie-Olympe-de-Gouges.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Blanche%20Peyron2%20%28cropped%29%20%28cropped%29.png",
"http://commons.wikimedia.org/wiki/Special:FilePath/Manuel%20-%20Colette.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Marquise%20de%20sevignee.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Imperatrice-eugenie-1864-s.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Philis%20de%20La%20Charce%20IMG%200499%20bis.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Simone%20Veil%2C%20gymnase%20Japy%202008%2002%2027%20n3%20ret.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Henri%20Lehmann%20-%20Portrait%20de%20Marie%20de%20Flavigny%2C%20comtesse%20d%27Agoult%20%281805-1876%29%2C%20%C3%A9crivain%20%28sous%20le%20pseudonyme%20de%20Daniel%20Stern%29%2C%20compagne%20de%20Liszt%20-%20CARP2170%20-%20Mus%C3%A9e%20Carnavalet.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Juliette%20gr%C3%A9co.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Judith%20Gautier%20circa%201880.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Fran%C3%A7oise%20Sagan%201960.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Fran%C3%A7oise%20Sagan%201960.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Louise%20Michel%2C%20grayscale.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Place%20de%20l%27%C3%A9glise%20Sainte-Blandine%20%28Is%C3%A8re%29.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Cl%C3%A9mence%20Lortet.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/BARDEY%20Jeanne.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Louise%20Michel%2C%20grayscale.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Dalida%201974.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Miss.Tic%202012.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Simone%20de%20Beauvoir%20photo.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Mathilde%20%E2%80%9CMissy%E2%80%9D%20de%20Morny.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Andr%C3%A9%20Adolphe-Eug%C3%A8ne%20Disd%C3%A9ri%20%28French%20-%20%28Rosa%20Bonheur%29%20-%20Google%20Art%20Project.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Pierre%20Woeiriot02.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Jane%20Dieulafoy%20photo.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Flora%20Tristan.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Marie-Madeleine%20Fourcade.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Francisco%20de%20Goya%20-%20Marceline%20Desbordes-Valmore.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Boilly%20-%20Portrait%20de%20M%C3%A9lanie%20Waldor.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/%C3%89lisabeth%20Vig%C3%A9e-Lebrun%20-%20selfportrait%20%28Kimbell%20Art%20Museum%2C%201781-2%29.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Christine%20de%20Pisan%20-%20cathedra.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Madame%20de%20Sable.gif",
"http://commons.wikimedia.org/wiki/Special:FilePath/Beguine%201489.png",
"http://commons.wikimedia.org/wiki/Special:FilePath/Simone%20Veil%2C%20gymnase%20Japy%202008%2002%2027%20n3%20ret.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Jeanne-albret-navarre.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Sophiedecondorcet.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Isadora%20Duncan%20portrait%20cropped.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Francisco%20de%20Goya%20-%20Marceline%20Desbordes-Valmore.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Agence%20Rol%20-%201910%20-%20Madame%20Hubertine%20Auclert.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Lucienne%20HEUVELMANS.jpeg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Baker%20Harcourt%201940%202.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Madeleine%20Pelletier%201.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Elsa-triolet-1925.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/%D0%9C%D0%B0%D1%80%D0%B8%D1%8F%20%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D1%8C%D0%B5%D0%B2%D0%B0.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Eileen%20Gray.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Sarah%20Bernhardt%20by%20Paul%20Nadar%20%28crop%29.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Jeanne%20Avril.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Tailleferre%20Harcourt%201937%202.jpg",
"http://commons.wikimedia.org/wiki/Special:FilePath/Gerda%20Taro-Anonymous.jpg"
]

for image in images:
      driver.get(image.replace("http://commons.wikimedia.org/wiki/Special:FilePath/","https://commons.wikimedia.org/wiki/File:"))
      time.sleep(2)
      # Get the smallest version of the picture
      try:
        image = driver.find_element_by_css_selector(".mw-filepage-other-resolutions .mw-thumbnail-link")
      except:
        image = driver.find_element_by_css_selector(".internal")
      print(image.get_attribute('href'))