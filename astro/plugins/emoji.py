# Astro-UB

from astro.utils import admin_cmd
from astro import CMD_HELP

basemojitext = [
    "a",
    "b",
    "c",
    "ç",
    "d",
    "e",
    "f",
    "g",
    "ğ",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "ö",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "ü",
    "v",
    "w",
    "x",
    "y",
    "z",
    "@",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

emojis = [
    "⁭\
    \n                    💖\
    \n                  💖💖\
    \n               💖💖💖\
    \n            💖💖 💖💖\
    \n          💖💖    💖💖\
    \n        💖💖       💖💖\
    \n      💖💖💖💖💖💖\
    \n     💖💖💖💖💖💖💖\
    \n   💖💖                 💖💖\
    \n  💖💖                    💖💖\
    \n💖💖                       💖💖\
    \n",
    "⁭\
    \n💗💗💗💗💗💗💗\
    \n💗💗💗💗💗💗💗💗\
    \n💗💗                     💗💗\
    \n💗💗                     💗💗\
    \n💗💗💗💗💗💗💗💗\
    \n💗💗💗💗💗💗💗💗\
    \n💗💗                     💗💗\
    \n💗💗                     💗💗\
    \n💗💗💗💗💗💗💗💗\
    \n💗💗💗💗💗💗💗\
    \n",
    "⁭\
    \n          💛💛💛💛💛💛\
    \n     💛💛💛💛💛💛💛💛\
    \n   💛💛                      💛💛\
    \n 💛💛\
    \n💛💛\
    \n💛💛\
    \n 💛💛\
    \n   💛💛                      💛💛\
    \n     💛💛💛💛💛💛💛💛\
    \n         💛💛💛💛💛💛\
    \n",
    "⁭\
    \n          💝💝💝💝💝💝\
    \n     💝💝💝💝💝💝💝💝\
    \n   💝💝                      💝💝\
    \n 💝💝\
    \n💝💝\
    \n💝💝\
    \n 💝💝\
    \n   💝💝                      💝💝\
    \n     💝💝💝💝💝💝💝💝\
    \n         💝💝💝💝💝💝\
    \n\
    \nㅤ               💝💝\
    \n",
    "⁭\
    \n💙💙💙💙💙💙💙\
    \n💙💙💙💙💙💙💙💙\
    \n💙💙                      💙💙\
    \n💙💙                         💙💙\
    \n💙💙                         💙💙\
    \n💙💙                         💙💙\
    \n💙💙                         💙💙\
    \n💙💙                      💙💙\
    \n💙💙💙💙💙💙💙💙\
    \n💙💙💙💙💙💙💙\
    \n",
    "⁭\
    \n💟💟💟💟💟💟💟💟\
    \n💟💟💟💟💟💟💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟💟💟💟💟\
    \n💟💟💟💟💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟💟💟💟💟💟💟\
    \n💟💟💟💟💟💟💟💟\
    \n",
    "⁭\
    \n💚💚💚💚💚💚💚💚\
    \n💚💚💚💚💚💚💚💚\
    \n💚💚\
    \n💚💚\
    \n💚💚💚💚💚💚\
    \n💚💚💚💚💚💚\
    \n💚💚\
    \n💚💚\
    \n💚💚\
    \n💚💚\
    \n",
    "⁭\
    \n          💜💜💜💜💜💜\
    \n     💜💜💜💜💜💜💜💜\
    \n   💜💜                     💜💜\
    \n 💜💜\
    \n💜💜                💜💜💜💜\
    \n💜💜                💜💜💜💜\
    \n 💜💜                        💜💜\
    \n   💜💜                      💜💜\
    \n     💜💜💜💜💜💜💜💜\
    \n          💜💜💜💜💜💜\
    \n",
    "\
    \nㅤ      🧡🧡🧡🧡🧡🧡\
    \n\
    \n          🧡🧡🧡🧡🧡🧡\
    \n     🧡🧡🧡🧡🧡🧡🧡🧡\
    \n   🧡🧡                     🧡🧡\
    \n 🧡🧡\
    \n🧡🧡                🧡🧡🧡🧡\
    \n🧡🧡                🧡🧡🧡🧡\
    \n 🧡🧡                        🧡🧡\
    \n   🧡🧡                      🧡🧡\
    \n     🧡🧡🧡🧡🧡🧡🧡🧡\
    \n          🧡🧡🧡🧡🧡🧡\
    \n",
    "⁭\
    \n💖💖                        💖💖\
    \n💖💖                        💖💖\
    \n💖💖                        💖💖\
    \n💖💖                        💖💖\
    \n💖💖💖💖💖💖💖💖💖\
    \n💖💖💖💖💖💖💖💖💖\
    \n💖💖                        💖💖\
    \n💖💖                        💖💖\
    \n💖💖                        💖💖\
    \n💖💖                        💖💖\
    \n",
    "⁭\
    \n💗💗💗💗💗💗\
    \n💗💗💗💗💗💗\
    \n          💗💗\
    \n          💗💗\
    \n          💗💗\
    \n          💗💗\
    \n          💗💗\
    \n          💗💗\
    \n💗💗💗💗💗💗\
    \n💗💗💗💗💗💗\
    \n",
    "⁭\
    \n         💛💛💛💛💛💛\
    \n         💛💛💛💛💛💛\
    \n                  💛💛\
    \n                  💛💛\
    \n                  💛💛\
    \n                  💛💛\
    \n💛💛          💛💛\
    \n  💛💛       💛💛\
    \n   💛💛💛💛💛\
    \n      💛💛💛💛\
    \n",
    "⁭\
    \n💙💙                  💙💙\
    \n💙💙             💙💙\
    \n💙💙        💙💙\
    \n💙💙   💙💙\
    \n💙💙💙💙\
    \n💙💙 💙💙\
    \n💙💙     💙💙\
    \n💙💙         💙💙\
    \n💙💙              💙💙\
    \n💙💙                   💙💙\
    \n",
    "⁭\
    \n💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟💟💟💟💟💟💟\
    \n💟💟💟💟💟💟💟💟\
    \n",
    "⁭\
    \n💚💚                                    💚💚\
    \n💚💚💚                         💚💚💚\
    \n💚💚💚💚               💚💚💚💚\
    \n💚💚    💚💚       💚💚    💚💚\
    \n💚💚          💚💚💚          💚💚\
    \n💚💚               💚                💚💚\
    \n💚💚                                     💚💚\
    \n💚💚                                     💚💚\
    \n💚💚                                     💚💚\
    \n💚💚                                      💚💚\
    \n",
    "⁭\
    \n💜💜                           💜💜\
    \n💜💜💜                      💜💜\
    \n💜💜💜💜                 💜💜\
    \n💜💜  💜💜               💜💜\
    \n💜💜     💜💜            💜💜\
    \n💜💜         💜💜        💜💜\
    \n💜💜             💜💜    💜💜\
    \n💜💜                 💜💜💜💜\
    \n💜💜                       💜💜💜\
    \n💜💜                             💜💜\
    \n",
    "⁭\
    \n           💖💖💖💖💖\
    \n     💖💖💖💖💖💖💖\
    \n   💖💖                   💖💖\
    \n 💖💖                       💖💖\
    \n💖💖                         💖💖\
    \n💖💖                         💖💖\
    \n 💖💖                       💖💖\
    \n   💖💖                   💖💖\
    \n      💖💖💖💖💖💖💖\
    \n            💖💖💖💖💖\
    \n",
    "\
    \n⁭ㅤ       ❤️❤️     ❤️❤️\
    \n\
    \n           ❤️❤️❤️❤️❤️\
    \n     ❤️❤️❤️❤️❤️❤️❤️\
    \n   ❤️❤️                   ❤️❤️\
    \n ❤️❤️                       ❤️❤️\
    \n❤️❤️                         ❤️❤️\
    \n❤️❤️                         ❤️❤️\
    \n ❤️❤️                       ❤️❤️\
    \n   ❤️❤️                   ❤️❤️\
    \n      ❤️❤️❤️❤️❤️❤️❤️\
    \n            ❤️❤️❤️❤️❤️\
    \n",
    "⁭\
    \n💗💗💗💗💗💗💗\
    \n💗💗💗💗💗💗💗💗\
    \n💗💗                     💗💗\
    \n💗💗                     💗💗\
    \n💗💗💗💗💗💗💗💗\
    \n💗💗💗💗💗💗💗\
    \n💗💗\
    \n💗💗\
    \n💗💗\
    \n💗💗\
    \n",
    "⁭\
    \n           💛💛💛💛💛\
    \n      💛💛💛💛💛💛💛\
    \n   💛💛                    💛💛\
    \n 💛💛                        💛💛\
    \n💛💛                           💛💛\
    \n💛💛              💛💛     💛💛\
    \n 💛💛               💛💛 💛💛\
    \n   💛💛                   💛💛\
    \n      💛💛💛💛💛💛💛💛\
    \n           💛💛💛💛💛   💛💛\
    \n",
    "⁭\
    \n💙💙💙💙💙💙💙\
    \n💙💙💙💙💙💙💙💙\
    \n💙💙                     💙💙\
    \n💙💙                     💙💙\
    \n💙💙💙💙💙💙💙💙\
    \n💙💙💙💙💙💙💙\
    \n💙💙    💙💙\
    \n💙💙         💙💙\
    \n💙💙              💙💙\
    \n💙💙                  💙💙\
    \n",
    "⁭\
    \n       💟💟💟💟💟\
    \n  💟💟💟💟💟💟💟\
    \n  💟💟                 💟💟\
    \n💟💟\
    \n  💟💟💟💟💟💟\
    \n      💟💟💟💟💟💟\
    \n                            💟💟\
    \n💟💟                 💟💟\
    \n  💟💟💟💟💟💟💟\
    \n       💟💟💟💟💟\
    \n",
    "⁭\
    \n💚💚💚💚💚💚💚💚\
    \n💚💚💚💚💚💚💚💚\
    \n               💚💚\
    \n               💚💚\
    \n               💚💚\
    \n               💚💚\
    \n               💚💚\
    \n               💚💚\
    \n               💚💚\
    \n",
    "⁭\
    \n💜💜                      💜💜\
    \n💜💜                      💜💜\
    \n💜💜                      💜💜\
    \n💜💜                      💜💜\
    \n💜💜                      💜💜\
    \n💜💜                      💜💜\
    \n💜💜                      💜💜\
    \n  💜💜                  💜💜\
    \n      💜💜💜💜💜💜\
    \n            💜💜💜💜\
    \n",
    "\
    \n⁭❤️❤️                      ❤️❤️\
    \n\
    \n❤️❤️                      ❤️❤️\
    \n❤️❤️                      ❤️❤️\
    \n❤️❤️                      ❤️❤️\
    \n❤️❤️                      ❤️❤️\
    \n❤️❤️                      ❤️❤️\
    \n❤️❤️                      ❤️❤️\
    \n❤️❤️                      ❤️❤️\
    \n  ❤️❤️                  ❤️❤️\
    \n      ❤️❤️❤️❤️❤️❤️\
    \n            ❤️❤️❤️❤️\
    \n",
    "⁭\
    \n💖💖                              💖💖\
    \n  💖💖                          💖💖\
    \n    💖💖                      💖💖\
    \n      💖💖                  💖💖\
    \n         💖💖              💖💖\
    \n           💖💖         💖💖\
    \n             💖💖     💖💖\
    \n               💖💖 💖💖\
    \n                  💖💖💖\
    \n                       💖\
    \n",
    "⁭\
    \n💗💗                               💗💗\
    \n💗💗                               💗💗\
    \n💗💗                               💗💗\
    \n💗💗                               💗💗\
    \n💗💗              💗            💗💗\
    \n 💗💗           💗💗          💗💗\
    \n 💗💗        💗💗💗       💗💗\
    \n  💗💗   💗💗  💗💗   💗💗\
    \n   💗💗💗💗      💗💗💗💗\
    \n    💗💗💗             💗💗💗\
    \n",
    "⁭\
    \n💛💛                    💛💛\
    \n   💛💛              💛💛\
    \n      💛💛        💛💛\
    \n         💛💛  💛💛\
    \n            💛💛💛\
    \n            💛💛💛\
    \n         💛💛 💛💛\
    \n      💛💛       💛💛\
    \n   💛💛             💛💛\
    \n💛💛                   💛💛\
    \n",
    "⁭\
    \n💙💙                    💙💙\
    \n   💙💙              💙💙\
    \n      💙💙        💙💙\
    \n         💙💙  💙💙\
    \n            💙💙💙\
    \n              💙💙\
    \n              💙💙\
    \n              💙💙\
    \n              💙💙\
    \n              💙💙\
    \n",
    "⁭\
    \n 💟💟💟💟💟💟💟\
    \n 💟💟💟💟💟💟💟\
    \n                       💟💟\
    \n                   💟💟\
    \n               💟💟\
    \n           💟💟\
    \n       💟💟\
    \n   💟💟\
    \n💟💟💟💟💟💟💟\
    \n💟💟💟💟💟💟💟\
    \n",
    "⁭\
    \n\
    \n⁭\
    \n\
    \n⁭\
    \n\
    \n",
    "⁭\
    \n       💗💗💗💗\
    \n   💗💗💗💗💗💗\
    \n💗💗               💗💗\
    \n💗💗               💗💗\
    \n💗💗               💗💗\
    \n💗💗               💗💗\
    \n💗💗               💗💗\
    \n💗💗               💗💗\
    \n   💗💗💗💗💗💗\
    \n        💗💗💗💗\
    \n",
    "⁭\
    \n          💙💙\
    \n     💙💙💙\
    \n💙💙 💙💙\
    \n          💙💙\
    \n          💙💙\
    \n          💙💙\
    \n          💙💙\
    \n          💙💙\
    \n     💙💙💙💙\
    \n     💙💙💙💙\
    \n",
    "⁭\
    \n    💟💟💟💟💟\
    \n  💟💟💟💟💟💟\
    \n💟💟          💟💟\
    \n                💟💟\
    \n             💟💟\
    \n          💟💟\
    \n       💟💟\
    \n    💟💟\
    \n  💟💟💟💟💟💟\
    \n  💟💟💟💟💟💟\
    \n",
    "⁭\
    \n     💛💛💛💛\
    \n  💛💛💛💛💛\
    \n💛💛         💛💛\
    \n                   💛💛\
    \n            💛💛💛\
    \n            💛💛💛\
    \n                   💛💛\
    \n💛💛         💛💛\
    \n  💛💛💛💛💛\
    \n     💛💛💛💛\
    \n",
    "⁭\
    \n                         💖💖\
    \n                    💖💖💖\
    \n              💖💖 💖💖\
    \n          💖💖     💖💖\
    \n     💖💖          💖💖\
    \n💖💖               💖💖\
    \n💖💖💖💖💖💖💖💖💖\
    \n💖💖💖💖💖💖💖💖💖\
    \n                         💖💖\
    \n                         💖💖\
    \n",
    "⁭\
    \n💚💚💚💚💚💚\
    \n💚💚💚💚💚💚\
    \n💚💚\
    \n 💚💚💚💚💚\
    \n   💚💚💚💚💚\
    \n                    💚💚\
    \n                    💚💚\
    \n💚💚          💚💚\
    \n  💚💚💚💚💚\
    \n     💚💚💚💚\
    \n",
    "⁭\
    \n        💜💜💜💜\
    \n    💜💜💜💜💜\
    \n💜💜\
    \n💜💜\
    \n💜💜💜💜💜💜\
    \n💜💜💜💜💜💜💜\
    \n💜💜               💜💜\
    \n💜💜               💜💜\
    \n    💜💜💜💜💜💜\
    \n        💜💜💜💜\
    \n",
    "⁭\
    \n💗💗💗💗💗💗💗\
    \n💗💗💗💗💗💗💗\
    \n                      💗💗\
    \n                     💗💗\
    \n                   💗💗\
    \n                 💗💗\
    \n               💗💗\
    \n             💗💗\
    \n           💗💗\
    \n         💗💗\
    \n",
    "⁭\
    \n        💙💙💙💙\
    \n   💙💙💙💙💙💙\
    \n💙💙               💙💙\
    \n💙💙               💙💙\
    \n   💙💙💙💙💙💙\
    \n   💙💙💙💙💙💙\
    \n💙💙               💙💙\
    \n💙💙               💙💙\
    \n   💙💙💙💙💙💙\
    \n        💙💙💙💙\
    \n",
    "⁭\
    \n        💟💟💟💟\
    \n   💟💟💟💟💟💟\
    \n💟💟               💟💟\
    \n💟💟               💟💟\
    \n 💟💟💟💟💟💟💟\
    \n      💟💟💟💟💟💟\
    \n                         💟💟\
    \n                        💟💟\
    \n  💟💟💟💟💟💟\
    \n       💟💟💟💟\
    \n",
]

cmojis = [
    "⁭\
    \n                    {e}\
    \n                  {e}{e}\
    \n               {e}{e}{e}\
    \n            {e}{e} {e}{e}\
    \n          {e}{e}    {e}{e}\
    \n        {e}{e}       {e}{e}\
    \n      {e}{e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                 {e}{e}\
    \n  {e}{e}                    {e}{e}\
    \n{e}{e}                       {e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n          {e}{e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                      {e}{e}\
    \n {e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n {e}{e}\
    \n   {e}{e}                      {e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n         {e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n          {e}{e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                      {e}{e}\
    \n {e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n {e}{e}\
    \n   {e}{e}                      {e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n         {e}{e}{e}{e}{e}{e}\
    \n\
    \nㅤ                 {e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n",
    "⁭\
    \n          {e}{e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                     {e}{e}\
    \n {e}{e}\
    \n{e}{e}                {e}{e}{e}{e}\
    \n{e}{e}                {e}{e}{e}{e}\
    \n {e}{e}                        {e}{e}\
    \n   {e}{e}                      {e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n          {e}{e}{e}{e}{e}{e}\
    \n",
    "\
    \nㅤ      {e}{e}{e}{e}{e}{e}\
    \n\
    \n          {e}{e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                     {e}{e}\
    \n {e}{e}\
    \n{e}{e}                {e}{e}{e}{e}\
    \n{e}{e}                {e}{e}{e}{e}\
    \n {e}{e}                        {e}{e}\
    \n   {e}{e}                      {e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n          {e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}                        {e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n          {e}{e}\
    \n          {e}{e}\
    \n          {e}{e}\
    \n          {e}{e}\
    \n          {e}{e}\
    \n          {e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n         {e}{e}{e}{e}{e}{e}\
    \n         {e}{e}{e}{e}{e}{e}\
    \n                   {e}{e}\
    \n                   {e}{e}\
    \n                   {e}{e}\
    \n                   {e}{e}\
    \n{e}{e}         {e}{e}\
    \n  {e}{e}       {e}{e}\
    \n   {e}{e}{e}{e}{e}\
    \n      {e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}                  {e}{e}\
    \n{e}{e}             {e}{e}\
    \n{e}{e}        {e}{e}\
    \n{e}{e}   {e}{e}\
    \n{e}{e}{e}{e}\
    \n{e}{e} {e}{e}\
    \n{e}{e}     {e}{e}\
    \n{e}{e}         {e}{e}\
    \n{e}{e}              {e}{e}\
    \n{e}{e}                   {e}{e}\
    \n",
    "⁭\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}                                {e}{e}\
    \n{e}{e}{e}                      {e}{e}{e}\
    \n{e}{e}{e}{e}            {e}{e}{e}{e}\
    \n{e}{e}    {e}{e}    {e}{e}    {e}{e}\
    \n{e}{e}        {e}{e}{e}         {e}{e}\
    \n{e}{e}             {e}              {e}{e}\
    \n{e}{e}                                {e}{e}\
    \n{e}{e}                                {e}{e}\
    \n{e}{e}                                {e}{e}\
    \n{e}{e}                                {e}{e}\
    \n",
    "⁭\
    \n{e}{e}                           {e}{e}\
    \n{e}{e}{e}                      {e}{e}\
    \n{e}{e}{e}{e}                 {e}{e}\
    \n{e}{e}  {e}{e}               {e}{e}\
    \n{e}{e}     {e}{e}            {e}{e}\
    \n{e}{e}         {e}{e}        {e}{e}\
    \n{e}{e}             {e}{e}    {e}{e}\
    \n{e}{e}                 {e}{e}{e}{e}\
    \n{e}{e}                     {e}{e}{e}\
    \n{e}{e}                           {e}{e}\
    \n",
    "⁭\
    \n           {e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                   {e}{e}\
    \n {e}{e}                       {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n {e}{e}                       {e}{e}\
    \n   {e}{e}                   {e}{e}\
    \n      {e}{e}{e}{e}{e}{e}{e}\
    \n            {e}{e}{e}{e}{e}\
    \n",
    "\
    \nㅤ       {e}{e}      {e}{e}\
    \n\
    \n           {e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                   {e}{e}\
    \n {e}{e}                       {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n {e}{e}                       {e}{e}\
    \n   {e}{e}                   {e}{e}\
    \n      {e}{e}{e}{e}{e}{e}{e}\
    \n            {e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n",
    "⁭\
    \n           {e}{e}{e}{e}{e}\
    \n      {e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                    {e}{e}\
    \n {e}{e}                        {e}{e}\
    \n{e}{e}                           {e}{e}\
    \n{e}{e}              {e}{e}     {e}{e}\
    \n {e}{e}               {e}{e} {e}{e}\
    \n   {e}{e}                   {e}{e}\
    \n      {e}{e}{e}{e}{e}{e}{e}{e}\
    \n           {e}{e}{e}{e}{e}   {e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}    {e}{e}\
    \n{e}{e}         {e}{e}\
    \n{e}{e}              {e}{e}\
    \n{e}{e}                  {e}{e}\
    \n",
    "⁭\
    \n       {e}{e}{e}{e}{e}\
    \n  {e}{e}{e}{e}{e}{e}{e}\
    \n  {e}{e}                 {e}{e}\
    \n{e}{e}\
    \n  {e}{e}{e}{e}{e}{e}\
    \n      {e}{e}{e}{e}{e}{e}\
    \n                            {e}{e}\
    \n{e}{e}                 {e}{e}\
    \n  {e}{e}{e}{e}{e}{e}{e}\
    \n       {e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n               {e}{e}\
    \n               {e}{e}\
    \n               {e}{e}\
    \n               {e}{e}\
    \n               {e}{e}\
    \n               {e}{e}\
    \n               {e}{e}\
    \n",
    "⁭\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n  {e}{e}                  {e}{e}\
    \n      {e}{e}{e}{e}{e}{e}\
    \n            {e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}                      {e}{e}\
    \n\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n  {e}{e}                  {e}{e}\
    \n      {e}{e}{e}{e}{e}{e}\
    \n            {e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}                              {e}{e}\
    \n  {e}{e}                          {e}{e}\
    \n    {e}{e}                      {e}{e}\
    \n      {e}{e}                  {e}{e}\
    \n         {e}{e}              {e}{e}\
    \n           {e}{e}         {e}{e}\
    \n             {e}{e}     {e}{e}\
    \n               {e}{e} {e}{e}\
    \n                  {e}{e}{e}\
    \n                       {e}\
    \n",
    "⁭\
    \n{e}{e}                               {e}{e}\
    \n{e}{e}                               {e}{e}\
    \n{e}{e}                               {e}{e}\
    \n{e}{e}                               {e}{e}\
    \n{e}{e}             {e}             {e}{e}\
    \n{e}{e}          {e}{e}           {e}{e}\
    \n{e}{e}       {e}{e}{e}         {e}{e}\
    \n{e}{e}    {e}{e}  {e}{e}     {e}{e}\
    \n {e}{e}{e}{e}        {e}{e}{e}{e}\
    \n    {e}{e}{e}              {e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}                    {e}{e}\
    \n   {e}{e}              {e}{e}\
    \n      {e}{e}        {e}{e}\
    \n         {e}{e}  {e}{e}\
    \n            {e}{e}{e}\
    \n            {e}{e}{e}\
    \n         {e}{e} {e}{e}\
    \n      {e}{e}       {e}{e}\
    \n   {e}{e}             {e}{e}\
    \n{e}{e}                   {e}{e}\
    \n",
    "⁭\
    \n{e}{e}                    {e}{e}\
    \n   {e}{e}              {e}{e}\
    \n      {e}{e}        {e}{e}\
    \n         {e}{e}  {e}{e}\
    \n            {e}{e}{e}\
    \n              {e}{e}\
    \n              {e}{e}\
    \n              {e}{e}\
    \n              {e}{e}\
    \n              {e}{e}\
    \n",
    "⁭\
    \n {e}{e}{e}{e}{e}{e}{e}\
    \n {e}{e}{e}{e}{e}{e}{e}\
    \n                       {e}{e}\
    \n                   {e}{e}\
    \n               {e}{e}\
    \n           {e}{e}\
    \n       {e}{e}\
    \n   {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n\
    \n⁭\
    \n\
    \n⁭\
    \n\
    \n",
    "⁭\
    \n       {e}{e}{e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n        {e}{e}{e}{e}\
    \n",
    "⁭\
    \n          {e}{e}\
    \n     {e}{e}{e}\
    \n{e}{e} {e}{e}\
    \n           {e}{e}\
    \n           {e}{e}\
    \n           {e}{e}\
    \n           {e}{e}\
    \n           {e}{e}\
    \n      {e}{e}{e}{e}\
    \n      {e}{e}{e}{e}\
    \n",
    "⁭\
    \n    {e}{e}{e}{e}{e}\
    \n  {e}{e}{e}{e}{e}{e}\
    \n{e}{e}          {e}{e}\
    \n                {e}{e}\
    \n             {e}{e}\
    \n          {e}{e}\
    \n       {e}{e}\
    \n    {e}{e}\
    \n  {e}{e}{e}{e}{e}{e}\
    \n  {e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n     {e}{e}{e}{e}\
    \n  {e}{e}{e}{e}{e}\
    \n{e}{e}         {e}{e}\
    \n                   {e}{e}\
    \n            {e}{e}{e}\
    \n            {e}{e}{e}\
    \n                   {e}{e}\
    \n{e}{e}         {e}{e}\
    \n  {e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}\
    \n",
    "⁭\
    \n                         {e}{e}\
    \n                    {e}{e}{e}\
    \n              {e}{e} {e}{e}\
    \n          {e}{e}     {e}{e}\
    \n     {e}{e}          {e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}{e}\
    \n                         {e}{e}\
    \n                         {e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n {e}{e}{e}{e}{e}\
    \n   {e}{e}{e}{e}{e}\
    \n                    {e}{e}\
    \n                    {e}{e}\
    \n{e}{e}          {e}{e}\
    \n  {e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}\
    \n",
    "⁭\
    \n        {e}{e}{e}{e}\
    \n    {e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n    {e}{e}{e}{e}{e}{e}\
    \n        {e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n                      {e}{e}\
    \n                     {e}{e}\
    \n                   {e}{e}\
    \n                 {e}{e}\
    \n               {e}{e}\
    \n             {e}{e}\
    \n           {e}{e}\
    \n         {e}{e}\
    \n",
    "⁭\
    \n        {e}{e}{e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n        {e}{e}{e}{e}\
    \n",
    "⁭\
    \n        {e}{e}{e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n {e}{e}{e}{e}{e}{e}{e}\
    \n      {e}{e}{e}{e}{e}{e}\
    \n                         {e}{e}\
    \n                        {e}{e}\
    \n  {e}{e}{e}{e}{e}{e}\
    \n       {e}{e}{e}{e}\
    \n",
]


@astro.on(admin_cmd(pattern=r"emoji ?(.*)"))
async def emoji(e):
    textx = await e.get_reply_message()
    message = e.pattern_match.group(1).strip()

    if message:
        pass

    elif textx:
        message = textx.text
    
    else:
        await e.edit(f"**👋 Give me a text!\
            \n\nℹ For example you should write like this:**\
            \n➡ `.emoji Astro`")
        return
    
    try:
        final = "  ".join(message).lower()
        for index in final:
            if index in basemojitext:
                text = emojis[basemojitext.index(index)]
                final = final.replace(index, text)
        await e.edit(final)
    
    except:
        await e.edit(f"**❎ Text is too big**")


@astro.on(admin_cmd(pattern=r"cemoji ?(.*)"))
async def cmoji(c):
    message = c.pattern_match.group(1).strip()

    if message:
        try:
            emoji, message = message.split(" ", 1)

        except:
            await c.edit(f"**👋 Give me a text!\
            \n\nℹ For example you should write like this:**\
                \n➡ `.cmoji 👋 Astro`")
            return

    else:
        if len(message) < 1:
            await c.edit(f"**👋👋 Give me a text!\
            \n\nℹ For example you should write like this:**\
                \n➡ `.cmoji 👋 Astro`")
            return

    try:
        final = "  ".join(message).lower()
        for index in final:
            if index in basemojitext:
                text = cmojis[basemojitext.index(index)].format(e=emoji)
                final = final.replace(
                    index, text
                )
        await c.edit(final)
    
    except:
        await c.edit(f"**❎ Text is too big!**")


CMD_HELP.update({"emoji": "➟ .emoji\nUse - Create a Name with Heart emoji\."
  "\n.cemoji\nUse - create a name with custom emoji"
})
