import wx
from wx.lib.embeddedimage import PyEmbeddedImage
catalog = {}
index = []

l_lar = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAAD6AAAA+gGwPyXs'
    b'AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAmFJREFUeJztmzFrFEEY'
    b'hp9vsheJEqxEUVPZWGmhJrbWFoq1cLd6BvwJotgYhPsDFt7hbQT7gBYiaC2KkJ8gGJJGQY0o'
    b'mr0ZmyhcwJtJbrkP3O+BK2Z5Z993Xxjm9vZWynb7F9BgMnzLer3ZkYoCD8hk4rDpJmjGhL2S'
    b'cNoBtLECtANoYwVoB9Am2/7EeOihP7abyCCqCSzgKtgtPDcRWhGv6ZSLR0Q+THe7r8cOlULO'
    b'20rO0+dSVCP42i8BK0A7gDZWgHYAbZJ2gRSa/eIZgRMp2iBSPM6bnT/jVr9/LnjppXqVPrv4'
    b'5MbVtb3k3EllBWxf/MkUqYRweMd4NoicSrXKGuW+Xab7J7VfAlaAdgBtrADtANpYAdoBtLEC'
    b'tANoYwVoB9Cm9gVkPoSFmKjhffzOK7AqEr6kmAbk/dBYZJPAaspcgHIr+xkVOR7gWYkEif9I'
    b'axiGYfzHCJ31s3gZ/SzOZ2vcPrQxStJ8VNwPyOkUUye+W+T53y2qWRRnGHAnKbHj03Leasdk'
    b'T5dmjk3BXEyXEdwbJPIwMvN3gXuRc50XwoWYIYDHvRw6UHIEx+WUuQTWU2SZk1yQWGb7JmgF'
    b'aAfQxgrQDqCNFaAdQBsrQDuANlaAdgBtal9Adf8Qgc/AxxSh8/770AFhC/ia6JOqS6KyApav'
    b'ta7see711gvgYFVZdkPtl4AVoB1AGytAO4A2ibtAOE5nY35sNx8G3Dr6bpTk+dLMfHBMje0V'
    b'mEt57SIDSmIvTgYWQRbHDiXyA9g/UuPcK4ED43slqcraLwErQDuANlaAdgBtqrwbrIoB4Cfl'
    b'9RsbE4JO+0yTOgAAAABJRU5ErkJggg==')

l_med = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAAC8AAAAvCAYAAABzJ5OsAAAACXBIWXMAAAC5AAAAuQHip0Ho'
    b'AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAkpJREFUaIHtmT9oE1EY'
    b'wH/f3aVpSISOwc3Bobujo4Ki4JTRRmwwIAgOgtbNRWMRRKiLPWpbtwwOilYRwVUcBCdBwbX+'
    b'oSA2NLlc3ucgRWjuRe6IuR7cbwrve+/7fhde3rv3ImGjEQIuY0KhVfD9haHAKneBy+OqA+w4'
    b'gIwxIaiON98InEkV+h/k8mnhAVuWWB/VZuyErvspMmBYxuV13HzAQzTyd9mXsNFQy6Cu5/ul'
    b'BMXGyyqG6EUlyPS0yeXTwksyqL6yekFVjlg7CB/Wz9eXAM4urx9yncGVUfkGBffGo7m5b3E9'
    b'EsmDHBPRmj3MM2AJQBytqsjFkdlU7wGx5TM9bXL5tMjl0yKXT4tMy3vAy8iIam+yKhaEDTTy'
    b'Sw48z/dPxM1XGASX+oXC8CF7t55qZ/ez45j3wOyofMVu74s1WOdUXL+cnBEkumOp3W9XKqVt'
    b'6xFRVLsr8/O/AGrttlvudA7Y+k4FgT5oNn8m8fBofX2OmOGHMBKwUD0TNahc6twxONbDuYiu'
    b'AecApre7RxV5Y+vbKxR7wLQtvnGr/ASlGC2PniTqkkvYF0ulKMexPFymN6lcPi1y+bTI5dMi'
    b'0/KJLp1U5Z2IzljjyNu/BcLvA9zHtr6iGiRxABBam7Yr7h7XqtZte1K8uFneId9h9xmZlveA'
    b'H0jEa6VKwOLm6dgZQ/OZ6wc/7m1+dbsyGw7M4dj5RLcUmRpqNn/kZ1CJXnUMT2MXc9xF4Ore'
    b'5kGodREZav8najkxCSbT0yaXT4uEf+vER8Ao2DbEJJjftFqj6HSMflIAAAAASUVORK5CYII=')


#----------------------------------------------------------------------
email = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAC'
    b'N0lEQVQ4jYWTW0gTUBjHf+fsohPRkeUlMy9Qa2wZhdJWVs5eIiLwpZ6CXnroNYjArCC6PiQE'
    b'IdFLD0EU9JgECW15FxIhxUtIzvCSzqUrUue2c3qwrW1O+j1+/+//Px8f3xFswYej1TahInap'
    b'Zb7WYtZojPTVdY//Su8T6QWf29kI3AbtTJPCGl6hDM2e/s/TmwI0yI9HHE/QXN5qqr8Ekbqx'
    b'vnukMyXA63I8EIJr/zHHCWmky9M7NGYE6DjsrFZCX03uMBdsp7jxPNnFO1mbnWb2zUuiP0Nx'
    b'OV+ingL1EiAm9RVAxtWsohJstx4S9Lbz5d4Ngp1ebDfvI81ZiQc0nOhw2Q8JAJ/b8R0oiot7'
    b'r99h5vULtrnqyLU7+T0xzuo3P8JgYOF9WyJEaNEse9xuS7IZwLJrN9HQEgXHG/C3tmApr2Rl'
    b'apLs0rKURWipK+SyNaA2JvqHikaxlFex4v+KeUchkaUf5FRUsR5cTA3QIiZPv5sIA3MpAWur'
    b'rAcDWMorsda4yd1jw1rrJtDelhIghZ7c2IHL8QzBpcSKD9ZQeu4Ck60thAPzmPLyCS/Mk44W'
    b'ar8RQBkMj6SKXQRMAKHBT0RCyxSeOovJamXR154p4K2nZ3Q4cUg+l7MJoe9ueiYTgkWtYrWe'
    b'vjG/IV57Pr3QNVVWZAbqyPBHkphRSp5p6B8ZhaTjEaDre4ebkJxE0AWoNOOyhsfRWOxAQ//Q'
    b'QJIvMx3H7CVKyX1K6zyjFnM569mDNQMDkfS+P0Eh0LUaa0RWAAAAAElFTkSuQmCC')

#----------------------------------------------------------------------
reuse_sheet = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'wklEQVQ4jcWSTUiUYRSFn/u+859TmpYxqKvIn9xMCWGZaC2CIAOFCMG1i6SScCGYfFDQqoSo'
    b'RbQJQl0YScsosKAWRYtIp0HaidUm6W9mdGa+731bKFN9mi29y8s5555zuLDVIxtuHVTzHnpj'
    b'SQ4AROp5dWwHU45g/NDARvx9HhcLH7keT0KkFsjB8xwJYOy/DpqvUutq0sA2HSNXdQJEiFlL'
    b'Tln6Zhp5+Cde+QVsBV9VmGkdBjxGMIxgQCwLxnDunxGOp6n0oNUaogJDS0+425Dg5fcQiXyR'
    b'AbE0KLVJhLYUdRruidAOXHvWxGU/+OAdgvkVLniG8fQgn/9yoMOMiUunGOYRDvvJ+2+wc2WZ'
    b'xxhaKNIK9JQ66MzSJZpuACsUgwW6/AL8IIMhalywRbr3jnKqJOBZyiUKVmMy75lcfMrJppsk'
    b'AdreUdGR4n7VWU7HW5gIV2NCNRCpZvfvDhzUkT6+FeaJZ2ZBBUECTM2d50xHigcoDgE1KCAE'
    b'rkv2xTjbcTBqTcDkPzH88+0641jBwyLIamNSBoUsl3BWv7JU4puj3K6/QloFqLQW8PgAIHn6'
    b'iXDLah7pGEg5X17vYmb9qa2aX0e8i7dckPlgAAAAAElFTkSuQmCC')

#----------------------------------------------------------------------
deactivate_it = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAA'
    b'1UlEQVQ4jcXSwUpCURDG8d8tQQxKlMhWEe1C3ATWKnqRVvlMvkXv0KY3KGhdFBGJ1VIjbHEn'
    b'kNM9Si3qg4EzHzN/zjDDf6vI+Ns4wTtmWMMlbtPC1YrmPfRxjpsAjHEYwNGyX51m/AMMUnMl'
    b'yZt4ygCu8Yb2MsB4Lt+KgCkesb4I8IDdeHdxHNENr4P7+YZaAvhQbqaFBibhN8IromahCpyh'
    b'jv2Ienjf1p67g030cBf5Dq5UrDAd4UsjHAWI8jYuqgpzAHjBK56V8/9YTQwjNn4D+Bt9Arvw'
    b'ISxN4oFyAAAAAElFTkSuQmCC')

#----------------------------------------------------------------------
note = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAA'
    b'nElEQVQ4jWNgGGjACGP8P8j+nySN9j8ZGRgYGJgodQELMufXVwaGP78IaGBjYGDjRvCp64Kf'
    b'XyCuwAfYuFFdgGIArziFLvj8EtMFbNz4DaauC/ACNgkGBl5DCPvzBQYGhgcMDAykxAKvIQOD'
    b'ykQGBkEPBobf75pgwqRF49vtDAx3y5oY7T7Vw4SIT8psEgwMv982Mdp9qcerju4AAOQCI0jh'
    b'EaD5AAAAAElFTkSuQmCC')

#----------------------------------------------------------------------
login_enter = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAC'
    b'FElEQVQ4jY2STUhUURTHf+e++2a0mvTZh0ybBiootJx0EVKGtgkjWkRSCBW2aNe+Xa4kKUiI'
    b'SMJAhCBomYtWQmGR4qSFleEnrWxhZak588Z3WjhvMinGs7u/e/4/zv1w2GDV19fbzZ63vywe'
    b'd+dmZ3+GXDYSrqyqPo/IPWBbDr3E4fJoKjVZUFBRVXNMhOeKdKnSKQQ7xcgtFLtQGqsuKDiY'
    b'rHkSCOXvh1PHQ5ZMJhNZnElBL5lCAoUKUfrXspGRkRmFzwp7CwoAFySzHgr4qmIsgJ65EstG'
    b'0ldBdqxvfDz/zdvluifq9h2YcSv29Ehra5DbyhpD1gL4rt8pSHMYCoo3EWwvw5n9woUSD6AO'
    b'1Tp/dDwG3AUIAlos/rQFENGGMLxw7ixLp06CMcjyL2Ldjyh6PZAbWxpCwYd3qQEAo43XokA5'
    b'wHLtEZZON4JZvZqPk9N8b7nISjwe+hPrj2jSW+d3AwYgczjJ17k5pibGedHXR8/DLtRa0ocq'
    b'/y9wVlbyUDIZHGvpaG/nWW8vN9racBwH8fOP4GlTU8lagVUxCVEFINr/ipKjtdzs6MB1I7iR'
    b'CGZxkWhqOB/ws9EE8DY/gah64SIy9omt9x8QW1jEdRzciSlKb9/BzP/IC8Qh3w9gA9GnRuU6'
    b'UApQNDhE0eAQiEBusj8lYzZdPPgXAdDmZi+bMVXo6sf6Z0mwZLfYN9LdvbwW/wZSZa3SlDT4'
    b'cQAAAABJRU5ErkJggg==')

#----------------------------------------------------------------------
return_it = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'OklEQVQ4jc2QMUtCYRSGn3OVS4OUDbd/EtFQKQRStOpsw61waWiK5taWCCQ1KmmxseZUguoH'
    b'1CJRQQXJLXARMuuehuTmDQ0Lgl74OJzD+z3vdz74d7Ls0tSQfRTr1W/4L5cXgUMVo79XgAAQ'
    b'vzCtQSeNMguAcopw5zMqTRepBFwjX90au/IBLLt0AMz0mPiiKiknO5HzVjBcXQauewEomIhu'
    b'WvPlcQ9QzUXPTfN1GKTcikk4mYi0H+O5EVJYanEMXF3xAAD3G5NPA331GKo7nZKr+Vj9MRNZ'
    b'A85ao1GAYLvpcn26ASTDyWK4+woignp9sJOpth2tfZ1ZqWJImiwoOvIxkRMPYM2V4igFhETX'
    b'2qTwmcsbqqu+P/iBGii2k40cey8wXL11Rfa/qyrsuUglGNDdh3T05hfBf6R3IKyD5zgW8F0A'
    b'AAAASUVORK5CYII=')

#----------------------------------------------------------------------
deman = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAA'
    b'xklEQVQ4jbXRPUoDQRgG4AesFqMMVpaBYKW4ggRzhRwhEE+Q2hvYC5aewc4uZUorbYRASGEl'
    b'BCKkDmyKrLAuK/uHH0w1PO+8M8M/zxBv+MITjuvgEbZIMusVoWpAFye4wUcupFOnScB7rslV'
    b'nYDHHP7GBFOEgxJ8iwiHWOMTD7jHOZZ/wVNcYGP/kH0cYZA2SNIGURG+xMr+6yYYZ/YCZngp'
    b'wz/3fS654q+Jc3iVBjbCa1xXxb2Ck+OqGO7aYDjDAvMmuPXsADDwOaajFSZqAAAAAElFTkSu'
    b'QmCC')

#----------------------------------------------------------------------
inventory = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAC'
    b'KklEQVQ4jZWQS2hTQRiFz8y9N7kxSaMxxGp1oUEx0iDYRlK0viiIK4uLggGxCl0JRSm6dWHx'
    b'gQsFi5tuBS2IdqMomCYElNoKuhArSl9R25Iq0kuT3My9M+NCEtIk9fHv/sOZM+f7SfuZh0c1'
    b'n9s/cvvYffzHdFwcOUvyxQXVlvwCmL0bQN2ArlM3M163sYlqIOG1M2zqR9PjgbvX40JYVwXY'
    b'OxUABCQBgHj3tZTmYfsBoAH5z3cGboQj67+I6K5x5X02hN7YA/3S8Hl/5Qdq5dLoMnAg/Eah'
    b'KsPEbMhV0tuDn9CxbbwuilotxJxz8Piz8FvWVElbWtgM3euFoplobZxOVfpJW/fQM8Xjjjpc'
    b'TuoAoxq1KABYQhMWHEInpkIJJ6UHJncKQVQhCZEilxv73UAI25z/njBLLmEHW3wTewtUaQCA'
    b'gL7E0/PRNKiaBQrQgoGkQnh/GUEC8tW9k/EyRufgoc49r5NzqhMAsHPdDE1NRvpHh3vK9Y/0'
    b'Pb9S9wal4cyBruYUFJXh7bcdq9lWD4Ck+JnZCt1rwDR8/xaw78RgrGXD1JM8zfiGvraKxOJ2'
    b'bhZ1cxlOd3NT5sXhvl6eno4cfPmoZ7RuABfQj4fG/JXsxuJGrWJXkpMR/Y8I1ex/u0XtDarZ'
    b'K/YAscA19SMACMaZZLZB2s49vaVIftrh1gkBsIbmVoSackVjCKnYAGAXLUvhuKwin0sIm28x'
    b'jWUGAIWaSrVKOYzID78Ay7HrOEz/pDMAAAAASUVORK5CYII=')

#----------------------------------------------------------------------
listit = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'NklEQVQ4jWNkwAFeXQ3l+fn3ux0DAwMDOzPnITHt1V+wqWOEMRQKlisEGMtY6soISbkKV/Rg'
    b'U7z7bUfJ5Sfvnm04++T4gwmRDxgYGBiYYJJMLEwJkvxcy0KNZbFqZmBgYAg1lu2R5OdaxsTC'
    b'lAATY8GmUEBhKQPD1y8MDN+/MjCIiOMyD7sBb9++Zfh2/iSD+M0LDO98Yhi27N8Cl/N2sCRs'
    b'AAMDAwPTjx8MX/xiGP5zcMM1SooKQ2Xf4TdAWFiYgcEnCO6FlFCfUS/Q3QtvP39j+Kyow8Dw'
    b'6QcDw6cfDIZaagzPXr1lkBARYvj9+zfDlx+/UC3D60Ek8O/fP4YzD98xLDn5CLcLtlx6ynDh'
    b'MTdWA/6cPsNw5uE7DHG4Af/+/Fvw+MPXA48/fMXtDGje/f+H4QFMCACm+ZMN5DKHawAAAABJ'
    b'RU5ErkJggg==')

#----------------------------------------------------------------------
delete_icon = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'dElEQVQ4jaWRO0sDQRSFv5lZN7uLkFio+ChUjKQWLCzFxsImlQ9Ei4ApgoUg+hvEdFqICDY2'
    b'VmlsrQUV/4ExiARjLJIgaDaPtYguu8Y1iKea4Z57HjPwT4igwev8wq4j5CiAcJr33ednO78K'
    b'OJlMhGp1DwgD1POFaS9RG+y/bBGdEoaxLeLxEoDmMmq1iWr2YS4oUSP74AqGxkeOgau2Cvmx'
    b'SSdIwIvB7K27p/kmSrZSAk1AfbkD8rvbJ6T3IqRCSIVcWyJ8ckDDsmhYFuGTA+Tqojv3wpdA'
    b'fCao3dxiphKIwzQARmyCcnqfLuXzCxbQ73I8pbYYPj0C4HFlHf0u51bsWKFhmEQ2ktTLFerl'
    b'SutsWj9W8AsoiVASPbmKGYtSTG5STG5ixqLoiWV37tvxXopTsw6AbRrQE0bPFwCwB/qQpQra'
    b'2zsAvdcXP3/jl3rItqFQdDuHnl9ahI6PKJUN6G0sP+xAATQ1Q5OhX9eVeOxg8Dd8ANxIYhcw'
    b'OF4DAAAAAElFTkSuQmCC')

#----------------------------------------------------------------------
all_sheets = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAA'
    b'7klEQVQ4jb3SPy+DURSA8V9LtAmJIJpULP4kTCYDu0+A1NbBxGASk+/Qb2EwkBiIWIQQBgmf'
    b'oAsxW9AYMLxX3PB6tRJ9krPcnPPcc869tIFBLKKjlaJhrOEYzzhA929FY9jABR6xhyr6IuFh'
    b'yPvGQijaRgU9kfAST5GwE0MoQD4IBrCPZUzgDDeYRg0lrKOMc9xhSbDFzGAVKzjCeOhuE1Nf'
    b'cotpghzucYprTKbNG5P/4by/meIsQdN8CBoh/kwXejGHK4ziLSNuMcvnEl9C1CXbT+MBO9jC'
    b'CV6zOhoJNzWwK3nKYisj5TAv+cb/yzurtDCi9TA7oQAAAABJRU5ErkJggg==')

#----------------------------------------------------------------------
new_sheet = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAC'
    b'MElEQVQ4jZWR309ScRjGHzgHiTgNFMub5kgrmlBTwIsoaclarpXZRq1VrotaF7l10T9Q86Kt'
    b'q9pqUW0sbdoKozZdhSNMUTA3cekiwfkD59CQQ7aBwDngoTtHgE6f2/f9PN/n+7w8bE98Y119'
    b'u4Qkq4NM7JbN7R7mNTZeaCjaIVRvheYxi8cUrFR/XrKX6owEAr7Vv1fISsUh07UbLfLNwEwm'
    b'gzfmh2jQptOW7gjpiocTV2VyuSk1/ZIUiSkwySQGHLaC8Jmmi+h59xSntctwuFbIU3oh7E5a'
    b'RK8wsVgm/YMEgNI9ZdCdMPwHSqTFKJHtxmvTfdRW+NHniqBGKYDHy8J4rpg1W2h71xfndRIA'
    b'Eok4QkvB3NywfXgObcUU+twRaFQCeLwpGI5KU21W+lPXR6cRAEcCwGo0ipkp3zp7uFqDkQEr'
    b'asp/weGioVYWYfQni3pdyZr5fajbYh28BIADAH7unwmCwH5FFca/D+NtTxhqZRHGvCwMOhl6'
    b'RyhfNgwAeR2IxRQmJzw4eUCEKMtD72Acl8+WYnT2IDTHdf143MZlP8jP7iC0FMQfOozJsSGU'
    b'7eKDEgjBMiKMB4+g+XYrhvq/qnITF+wgmkxjQqhClb4O9+7UYqeYKnjidYPyfZVovtmy4dJm'
    b'IreytDA/B5ZlwLIMsW2Db/bP8Pr9WJyf4dYYxp47zztjrpZDv0GQAo5LpZ90tptb8xIsBObC'
    b'zx492NAgMDstJoTCjo5XL+4Wmv8D4oHlon3pFq0AAAAASUVORK5CYII=')

#----------------------------------------------------------------------
logout = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'TklEQVQ4jbWTv0sCcRjGn/e+V0rQGdrQVEQWBQ6Bji1CDc3ln9Ciww1CPwbB3e0mqcHdv0KI'
    b'a2qsIaKjoaUCyavATO9pqJMzzguEPtP7g/d5ny9fXsEPLDQV5rR1aMyCkgWRheBcTvdPEIHe'
    b'qbeKM/dvFXY+5mVAHZTvjgDva4mE4zjJ4IDneZV0Ov00FJBPL6e3uwth6n1jOkMy86tcY60K'
    b'eJiWo+qDHmVvLFSzUIMYAEwkIIeVOz/WJnIQIFxgazlyyDRZLJWYAsY9wYiNpK6ro9FY9NNb'
    b'AFAKB+Uyd8Id3DxHOvDpdsFwB/HRsmH0YZoOAIDkqmWtbCuFpmVJO1zg+jFys2VJ3Y//6Rf+'
    b'wLa5adtcmlig18OLCF4BQOeUdtlPxneVf0wBdLd3JSIXwRpJN5+X4THJsFFoKqT0DQyYgzAH'
    b'IAdKS872jqPcfAEJkG4IwMSEXAAAAABJRU5ErkJggg==')

#----------------------------------------------------------------------
ez_label = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'hUlEQVQ4jb1STUsCURQ9M/PMQZlsDBs1JEeiDGGIFmFQBC37A+1b9A+CFhW07h+0aF2LVkG7'
    b'IEgMAlESiSgoM6yRysYha5rXTKvMvqYv6MBdXO49595z32PQhKXVjUWf4A3BAZp+ez41MT79'
    b'nJPmYiQUSCaVnuGt7R30KwlIkoRa/b5R97d6sJnOppo57NsJF2oFPO9Gbq8AQlh4+ZZGcMy7'
    b'9tcbAEC0KwIACEodTk4+FqhqurB3cAwAqBXLHxLUqxv/pxZEn6APKnE8PhgonpwiHBCxsraO'
    b'cEBEKr2LQSUOqb3t+lOB34CZWVweE7zCvMtF2GBAGOiVO71OhMJhsX5ZvcuYJrU0vb5AeDc/'
    b'mUj0jVJKwVn3UOLdjhPLFc3j84dGOI5DLpefJAzLAQBOS2dQVRW3d4ajQH7/CJIUREzuAsOx'
    b'TOMVYnIUMTn6peehZPur/M9H/H8BN6GIiC9fgTVN07Lt7wsYlKBU9cO2AWrSR6Ib1mwmm0ML'
    b'cTE/2eSBmrZuWHNPlmp8QFSg2T4AAAAASUVORK5CYII=')

#----------------------------------------------------------------------
reset = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'tUlEQVQ4jaWSy0tUARTGf+fOzB0HrBAfcQexRYpDouGujSC0cCliuNGFtGgzzCp8tLtBixoK'
    b'AjFwp4QbXajL+gPEhSB3ymR0oRXMBXtA6TQ5j3ta1K2pMRjHb3Xg4/zOdw4Hzinxi4sD8w8K'
    b'6s3lXt5+3zq93e5p6ZaqXBXRIJBWlTU32b3zX8CFgQUlHBqvj3XdBBlTcAW2gSLQC1xGWTz5'
    b'Hol/nun4eirAbGs7MBsaI6jG3YP0KssjJQBsNazj14Ni6KzCYQGz72MydgRglMfRbK7p2+7u'
    b'/aNXjhH5chz9bdjiuY+7V5DADYGWECezvlUO2C98+lDv5bLPRHUpRPDOv/tmHnW9U0/iIKPR'
    b'e6lYVVeukK2GNZlyo1Op6YoVqgOIB+J40FEbAEBURFVrTKAGSo8gezUBrGxqCGgBXYWyP2hP'
    b'7IWzkdxDSsGn7pNrb09tvvvmCoHihsCLTLJn/K8E4ca8gvZroLhuTTjD2Ponna2GNeEMEyhu'
    b'AG4eM+FbUj6hYWrzUp2GZkDGgENg65fVCzQLPM9jJvwvrAD4ik46nYgMetBp/Ey5g+paJnk9'
    b'Xd2lzqAftvGh5zdFr8kAAAAASUVORK5CYII=')

#----------------------------------------------------------------------
search_all = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAC'
    b'bklEQVQ4jZWSTU9TQRSGn7m9vS3ENuVDMBoKkiJtkI1xIUSjxg0WDYliTQhCjBFj4saFP8B/'
    b'4BJdsNAYEoGFQXSDJgRD0IUhCBZBGlohVL4CFijtvbfjQrnYsjC+qzkz8z7nzDkjyFHL8HiB'
    b'5orfl3aj1rbmjTjW/EOmYht8clls594FENZKSqV94k2f7ok0STUpAPJmG9BWA0hY1wunurpO'
    b'1zxAiMx+gJTixnTvN8M9V/n3oWLk4/p0B6Ngli1fP2rCG3l27FrV3xAF4ObY0NNcM0BG3QZh'
    b'ki4Og5AY7mhl+8SrvqwkHf0yX5uvv+SIn0D9WbbvjXrRV9SNCitOe6JNbR8Gi3ZjVZjmBSEU'
    b'jzN2FhQdvWAWM28NveQzGWUH21YpSrIIbbmGncOjpI6MCsUp7wEPAdRU+fD1TP4y9hU/ynYx'
    b'9lU/dsA5X59dihQ4F+pwLtQhEQmrAunY9OjuKLo7CkBe5CLait/yHY9PEJx6TWkizg/XIQb8'
    b'QSZLa6UFwLSPAY17czGzzLfD3SRCzSS8XtyxKB093XxcHC/s3G1iOuV4hOmwiMmKdxju7wAE'
    b'wwMkQs3oPh9S09B9VSSar3IqOtJgTaH75PkV+/rR/r0KDPSDkwCUbC5heL1ZrTC8XoSU1RYA'
    b'IFmTvKJulM3tbtrWywFYOlCCGotmAdRYDCCcBegRIXOnWvHZVwMvMZ0S2+8+DAQacb3owz4z'
    b'g0in0aancfX2wWZqUf75xYIc3RoZKVQ3AudEyl0OEBrr9pyJvg+KjPQj+MJmalEm9SYBj20D'
    b'z+/uA/xLEoTZ2NopkR1Cyrb/BliQYEurTc28/QWkEvLXo+pyHQAAAABJRU5ErkJggg==')

#----------------------------------------------------------------------
submit = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'EUlEQVQ4jd2Qvy4EYRTFf/ebEX8SnYIYkSwSD0GiWBVvQEIoEAmVbsqNSrOJYiUkI1Gr0IgO'
    b'z6BANmZFIQqKySRm5iq+2AxGdltOd88599yTC38e8qty+FhGs2kQh0yOWRq8bj8gCKvARo5R'
    b'RHwWvO3WAfbyOcBqyQWgdp/YEIiBC9x4jvmxNwDrOHjuxY3L9lY2BbA56rJW6gCg00D1NhGg'
    b'G5gl7dph726LlZFX4ajhkeolyvBniZl+h4k+Q5TauceBq5eMk6c037WBJpNCEO4C63nFCGQK'
    b'/rhtULl5b3JfoTWD4n2nfxqLOVQGDCJnBRIA9UipR0WbTZwKqkIQ+hhZzv+hBR5Q3WdxqNKm'
    b'/1/jA2syWgLOV6ztAAAAAElFTkSuQmCC')

#----------------------------------------------------------------------
price = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'3klEQVQ4jbWSvU9TURjGf+fcWy3NFSuNlAUhMSYCgxE/0MGPSGLc/AscZHF2MdE4dDQ6OJEo'
    b'upi4OphoonFDg9AuJpq2g0ggigjlo8WUe3vvOcehF1u4d3Dx3c6b5/297/PkwP+ol59HsgAT'
    b'eYYm8gwBPJ2iK04rY5v2vvEP8zcXtGFaG6YfzfApkNz7ZwD4z7LO6V5bphzAAY4heR6ntOOa'
    b'h14VzqrKpB5JQN1BSUPDKC4Ck7u1ov2RM8jjX84/6XtXvG5qFZG/AqalUAjuL53ibk6gYy8Y'
    b'Ll14nCn9GqvLGstHwfVAa+hIAWBhuN1TAOBOJIMXxRPDtnTGkl9nMarBUheUylAug+u2bTHc'
    b'Gv/IQASQEJ037MUFuXbQJ9GA1aDZP3wEkskdti1juBYBCCEH7UqF3+lmMpkM9PfDt1lYWWlN'
    b'u3VY+8HJCAAtzPoBn/VuMAY2NmBuDowGx2kBfA+QMSEub8288Ts3zzXPgXQaBgfCEDvCHQq8'
    b'OkjBVARQ9TYfpixGgUvFM2FeGgIPalugVLgd3juaB3+tt6eTM8ieApeBUeXTu7pINlRUDXy3'
    b'bN4GV3nd/g92AAAL2A8kw+sS29aBAHCBKqAiFsLqBvqAvcCeXYAG4AHzwM/tgT/4c6ro7pHq'
    b'AAAAAABJRU5ErkJggg==')

#----------------------------------------------------------------------
pics = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'DklEQVQ4jaXTu0pDURCF4c8L2ljZKAEFrdTOxktrqXkG8VKkzDOIIL5AOi/gGwg2KbS2EkkX'
    b'jDZ2tkKIKNEiEzhudiTgwDT/zF5rzjCHf8bIH3wO4wl/xecwwsf4zuRt2jgWblc4xwqmcJpx'
    b'hwV8oYM3dOESdyjhoeDWQBXbOEA9maaBefjAI7bwHMWzmKCEHSzFBJVw7Ytcy3xnIx4fxqh9'
    b'XguRiwJ7zwlUw7mTqZWxVmSjmUW1sIrJTG0TT0WQE5iJXeSihdkUpmPWg9cSfo8JHCX811b7'
    b'WQmRMk6wH4830C70daGZEejq3cc6prEczu2krynUc2c7TO71f6YydrE4YHlpvOid/82Q/YPj'
    b'B/P+dNRX2bgXAAAAAElFTkSuQmCC')

#----------------------------------------------------------------------
remove_item = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAA'
    b'6klEQVQ4jaXSv0oDQRDH8c/FINilSGGleIgQVLQQ0oqIjU+gL5HaB7K1FcE3UNDWTptYCSKK'
    b'gn/O4uZgOTm8IwPDDsP+vjM7s8xocw35PXzhpQusj2PcoMBJF/Ey7kNY+SuO2gIGuKsBCnzj'
    b'sC1kBdMQvuEj4gfMt4Vs4RmnGMZZYL8toIKsRdzDJSZNl9M1biPHNZ4iVyiHO8RV5MZYxGMK'
    b'yvEZgt1akYWAww5+lMPdqFqkXGM/4tUa4B23SaEsdLlElNpI89A2G/LW/f0D//k4BWQ46yC+'
    b'iGfIEkgPB1hqajNsinPlIGe3XxssRAgo6eKWAAAAAElFTkSuQmCC')

#----------------------------------------------------------------------
sn = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'AElEQVQ4jWNgoBAwMzAw6DAwMPgzMDC8YGBg+EykPikGBoYIBgaGn4xyyqp74gvLTlq7ej0X'
    b'Fpf4RYzuty9fsB3dvU1yYX+XOYuNl6+ClZun83+G/wxvXj0nzn5GBgYrN0+Guzev32U89fHP'
    b'nlMH9joT6XQUYObgvJeJHI3IYLgZwMbOwcDGzoFTMTZ5FmSOgaU1AwMDA8OF40cZGBgYGFS0'
    b'dRgYGBgY7ly9giJ/6sBe7AZ8/fyJgYGBgUFVRxfFFhgfJo8MGKNyi+7E5hYp43Q3HrB4ct9d'
    b'liPbNj9QVtdcSU5SPrJtszkDAwODNgMDQyoDJIMQC6SgerRIdjY6AADRmUlJWZWa9AAAAABJ'
    b'RU5ErkJggg==')

#----------------------------------------------------------------------
group_it = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAC'
    b'vUlEQVQ4jaWTSWhUWRSGv3vfqylalZSRqC3OQcFgxAkHbMTWTRR14YBNL5patEGlEqMigi6y'
    b'sGmFpqNFwNhuRGkVQUQIDgvjIk5RUDukNcYQqyqlqQwmxqR89fKq7u2FGkHjKv/yX3yc85/z'
    b'wyglvjZ02YlFaFGC0G60yCCVC2gg+O6aqKxU3wXoHady8VmHUPIJA/4r4kwoDaArKyV9eSvR'
    b'YgtSnRTHK55/A9AHjvlJe4+GV5XcfeyIdYPWh+rG0PwHAMU3k2MmGObvfS2JbENzvS1R50Wk'
    b'vOkzQAJg+Q4e+nF1bYuUZz+0t/9idw/UF136zw0w2WXU2u3R8sFkYu+iOSumoEWp3nHKNQzQ'
    b'FVUzgUTdkGdp58t2YzBjoq2U6e6yJwF0tL4u7km+RwkDR6kipDqNz/r5ywRZuQHHdVnrvr+y'
    b'iG7vu9faVzDu7sS5UyPFNf+2qqy4IVJ9ymVgj/Hm7Ad2ocVpXX78lt5dnW8CQVGzs4saAAoA'
    b'1t9+eyYVj/3qdCYhkJ///MhmA0CHI2sRorQrkMv9wtk/bXr8qNwc6bbxZ7EZKtaCoRXZsXn6'
    b'S+RaX124hEGvh+0P7n2ywpEyHNfFdRvX9mtPsL4nmlxgp+1HKuuMxXHyCmbPvCIloURz3JUb'
    b'CKy/96xuq1QqJDR3MLLbTMxsLVJtscnx29HYknSyB0t4lwcC/ulP9i2Ljb8aj6dexfyiv5+U'
    b'2/zTyOgQUt8XkT1nAaSoqmhDyck/vGhN9LbFEb1deJSdGSrwdAB0t71RVrQNIz2A26AJoX/D'
    b'8l34vNXHDHzW0XPRp8e2Fi4ua5HT1pim8UfjtqIhgExOcLExa17EC28evqh3gH/E36XOt68c'
    b'jgSQ6jDQiFSXRdVea/iVe4OrgM0oWS2qw80jdmEYtKdqIUqWAB60yCC0iRYN5PdeH6lMo9b/'
    b'FI0xqD2KNocAAAAASUVORK5CYII=')

#----------------------------------------------------------------------
search_my = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'AklEQVQ4jb3SMSuFURwG8N/lEmK6SgYGWW5KTAxieYcr252k5BtYfAKTlN1qs8gnsNjMiohs'
    b'irqJlcjwnlun09u5g/LUqXOe/3Oe85z/OfwRtUxtEsOZ+jve+jKCVo/DW1DPCD7wlKkv9DKA'
    b'Iawk3Bcuu4sqgzramMMSxnCK51D/TsUptnCGBzQCt4895bWymMBqBT+KExRYC1y7KsEs7sN8'
    b'MUoAn7hInVODO2V3X/ESRW4EbSFpYvoPatjGTMQN4hBHuFK+TNHVxD9xHBvoYArTGAjjIKRq'
    b'Bu0ujnEdb97BuvL5CE1K0MQ55uPIsIkf3IQBy8ruxxjBI25T5/4K8f/gFxcKJ6L0GRuAAAAA'
    b'AElFTkSuQmCC')

#----------------------------------------------------------------------
pdf = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAA'
    b'90lEQVQ4jcWQPUuCURiGr/M+imApOAiKNvcxh+IPsCH/gYboYPSjrIZoixabDQpaIsG9QFAH'
    b'ZzUk3+NpiBc/8P2goe7pOc997ov7HPhvKWcYFo6boGqA+GQ0iuvMy2sDwFphBQkDCIa6c7DW'
    b'jA3tnlWRdHo7ZAtg44oQyu4RyRc867gDtEaSSRaj0S8BgKRSGIwnIORmRHJ55h/vRIsnSCIB'
    b'SvHV7WIP+v4NwvsHxM4vsAdDPh9aYAlWLM5OueLfIHpaInx4xOyxzeT25mfZeQv+hMV4jN3r'
    b'Mb2/cw25ATQgs+enIDntDMs/MFytGl5hA5eB6v2JvgEaJTofKRHDyAAAAABJRU5ErkJggg==')

#----------------------------------------------------------------------
editit = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'XElEQVQ4jaWPPUgCYRzGf3caBafnUCFN0VhUQxQVRFS4J7S1RORY6NTHpkNYElS4HrgHDVJT'
    b'CAUV0hCUQQQtQjVEU4dafpzXYPlx3InQAy/vy/v+f8/7PPBPCdVTLLnWdHJ5MmppkBqYVZXe'
    b'aWdWyyLZJMx2/+utOvx47jIa2AFyaZdzMX3fNEAOl2yZQD1Gb0r/Sl6ozEvzG0PZ+O4DgAjQ'
    b'0Q6lIhTy5qtUrMwArEaP/LogpCTv1nq1AoDD0UKEWDLYP9Iz4818XcdvnmoVCqfoqgrlsjkn'
    b'irAv+tj+9gGwM+gObI72HTYkEEXrjyOaj0ihAiMIwT+4pQqhTCPM0nio/r1phYjmY0+vwAFN'
    b'4WBFETCoGlwUG9ddm6cK+zWFcKdimtCywpg8x8lngsR7mnCXgs1uRA0G9RXyZTsvH2dMOJ7x'
    b'dL9hs5nD9QZXssxU7bqEmwvj7KW1zT/0A2lHgOSt93qaAAAAAElFTkSuQmCC')

#----------------------------------------------------------------------
my_sheets = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAC'
    b'L0lEQVQ4jX2TT0hUURTGf/f9KVFLSpvBadDUMYRmmMwa00VFJQhRFNRScOFOQtpEi6AwWkQb'
    b'V7VRbNF+KIIocdFfpTCckgoEpajJyVLfdRSfvvduC6mceTIfXA7ncM53zrnfvVAAUspyKWV5'
    b'oRyxWTCdThcbhnEpk56/qjxPLyrVB3Rdv1JXV2cVJFBKCcuyLszNyb6h+8OVu39MIzyPb8Fq'
    b'jnecnHeclZsNDQ19QgjXR2BZVmJ5eeXOswevm+S7CU6FDL7EWgGo+TDC8KzDan09J861TC4u'
    b'yovRaPQJgLAsa6dt2/2fx6fPjj96IU5vWWShMUE2eoBd4SBKwVzmN8ZEiuDYS4ZWigkfPaT2'
    b'7q8ampmZ6RCZTOb6w/7H1+I/p9gajyPjCSqqQmi6lrOr53r8+ppme+oNdipFKlBLpLV6QLNt'
    b'u3Q2u8Zgtgy3rZ1ATdhXDKDpGoGaMG5bO4PZMmaza3ieV6J3d3cvNR+JHbMdtSNcX4tu6IVU'
    b'A6XQnWXOnG/+nkwm7xmRSOSVlLITeA5wNwVNQRjLQFcM9t26nFM/2dkDQDKZvNHb29tv5Iva'
    b'FIRQaeEhAEzTdACVu6xa75zOrtuNWFhTTC15PiIjP9AVW7eNATA30JsCinTBUl6+77pN7f/Z'
    b'iBJDECryv/y/EyhNCEaejmKYeSpU7Mlx345+RDMFSin1j8B13YnDLbWflBIVvhYHK3PcBOA4'
    b'qws9PbffQ+5nMoFtPoLN4QIWwB8m9dUKHKN1bAAAAABJRU5ErkJggg==')

#----------------------------------------------------------------------
activate_it = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'7ElEQVQ4jcWSvWsTcRjHv7m3xmvVprnkqFxySK6lIaitVVJwEbdOHRQR1KXgP9D4B6i7OFlc'
    b'1K2gDnVxc3GxqNVDJUTPu6RJiobci02N8ZLci4sXgr3O/W7Ph8/vy/PADzjoRMLg4uJ54Vw+'
    b'czstcjnHcUdqVevLx2Ltzvr6y9L/LjVcJmRymfysMHLl0pnnF5dOSQBQrpiw59OzM1l+gWUO'
    b'XX61Wf65rRU1AD4AkMFrSZpLbKUmGjcuTD9evr6QD3gsxiLBjcH3Me54bvrJj9+rEhWLW1aj'
    b'AwBEIKqqbB6v/omfPCGcDjtreiqJjMidTWmtpKrKZsAHBaKY5QmifTgxMXo0YLrRhm60AQAM'
    b'TSLJj7EM02NFMcvvKaDpqNPvE2bpW3MLABStiU25jncfalC0JgCgXLUq3Sgsmo46ewpUVdZJ'
    b'0mc23mpPW7u22++58DwPANDvuWjt2u7rN9ozuhOhVVXWw86EJElHAEQKK1cf2jtr/tdP933l'
    b'86pv76z5NwvXHgGI/HMGIYcHy7K6AKDr1Mb8nLAcj4+yJEmgWGqYt+69WPplmp3ACTL8DwZR'
    b'VVm/+yArc7yQAwCjsV38rihGmEuEQQDoelR9nEtNHkvPTHZ9qr6fF7oBAJTeywW9aU0BhG/U'
    b'K4X9vIPPXxQTw6ac8uOrAAAAAElFTkSuQmCC')

#----------------------------------------------------------------------
trash = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAA'
    b'60lEQVQ4jZ3RTSuEURjG8R8zkZdSpEzJQrGysWIhvgOJjzBLH0GWSspSsbKRhezkQ9ibjZ2d'
    b'HZImLOY50+nxnPNMrroX576u+3/eGtJqYAcTRZ1hE/N4rBpYwGy0PsBPUe84xzqOC2BfMzjC'
    b'Nx6i/iE+IkioT5xiJQRXS4F2BJnEHm6KU5RBcyF4ERkn1U9iHLu4xhu6mA7mCLawiNEEINYY'
    b'NgbI1Wso0d/Hds3sJe6bCbOld9+cbiEFuNJ7l5zucuayv/9frqkcoImvzPBLCA4nAF08Zzbo'
    b'1AHgaRDvv4BOxutrDa+q778UQr87x0H72ftTIQAAAABJRU5ErkJggg==')

#----------------------------------------------------------------------
logit = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'JUlEQVQ4jb2PvUoDURCFv4k3KGtAQWxErfQB1HrDWknEzsZn8AWs1cpSBIt0FnZWFokgxhAS'
    b'LK3SmMbCzkJCzC7GcMdmQy5bbH4KD1y458ycMzPwnwiC9kZSy4xr9v3OkbUzrXz++8H3u9sT'
    b'BQSBGhE5i+meiN4Paga4AVZS/E3VsAlsDgQRuQYugQUDrAO7KdPnrO2+OdJnvx9eAR3geeQJ'
    b'qt1jYG3I9bzRWO4MuBvgASXgMX47hYLOQuYFeIp73nO5XNEdYJx/COy7xSiKVlXtLXAqwoWq'
    b'ZMtl+XF7UjeoVr0PoA0UQf1abb6UPDF1AwBjMge9Xi+s1xe/krVkgAfcAVm3oVLxkp5f4BCI'
    b'xtpgFAxggZNJjTGsAEvA1pQBr1P6hvgDzfxZ6FRZzLoAAAAASUVORK5CYII=')

#----------------------------------------------------------------------
printer = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'tElEQVQ4jWNkgAIVOcVQJVXl6SKiIt8ZsID79+7dOn7qlDM2ObgB27Zs/Y8LONnbH8Omjwmn'
    b'iUQCJgYGBgZLffm9SlL/puNT+PH9S319dfkPWA3gZGfgLAj8L4zPAF01oe/aCv8/o4szOpvJ'
    b'twrxMSRwczCwM3BI4zTg/693///++vHv+bv/tx6+Y3W5c+fOTwYGBgYWAR7GmFVVf6UYuFQY'
    b'GBj+MzDIpjIwPJ6NSXPbMjC83sGwbD8TX+2i384MDAzbGBgYGFjYWf9BAvLbHYhVNyuw09/u'
    b'MjAwMDAI8vznYGBgdlaRU+RmYGBgYMHnb1xAQ0W+SFSQn+Hi9Tvv4AZceSZBUKOc4AcGBoaf'
    b'DKKC/Ayy0uIMtx48+gY3YNouJYZnbz7i1MzLxcFQHsDAwMDwEkUcbsC3bz8Y0rNyGTy9vbAa'
    b'EODtCWdnF5cx3LtxhWHv0dMMjPrq8h+0Ff5/fvaeg7+srp+Xj5uN4fH9uyiaIxLTGcwMtP8o'
    b'in9//eHTPzYZNVuW9+/ffbt27SYXXBG5eQEjFo4e2IPVBbgAigHnz59nMDQ0ZOAXk0VRtH3r'
    b'NpwGAACB+sDRJmEnwwAAAABJRU5ErkJggg==')

#----------------------------------------------------------------------
manage_users = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAC'
    b'QklEQVQ4jdWSTUhUYRSG32/mzs3xd2aaHNNupmSkghAEtanUgpCKKLCFi/4WQRs3gVAt2ga1'
    b'aGEEFpm0EYOIFlJGRC2aBIugwBKz8G9Gm3R+undm7vd957TQNNzWphfO5j0Pz+oF/vsIAPhw'
    b'qTySTothleNyBrqb78x3AcCrc+XnlWRLZPlhS39iZORyVbuTkL2kmIRr7Np3PzYqAOBtV8Vg'
    b'SVVpm3QIydlsbCHPWytKKWqndBNLgFhMKhINGyxjbF2Jv9LnE4iPZZ7s7Ym3GQAQriv+XtVU'
    b'C+E18ePLtPr46FtNeEfYqq+LQAhg+n2seOzpomUdqeRQrQVSLszSr7PoicMDAEHLFyPlglQe'
    b'RWGRz9ieyVB1oMQfCKKgLIjI9vUlJoypwrAnTyoP1i5C1d45AEsCyOw9OzXjOMlpSDt57ejj'
    b'RMYoIKVlFlpm4fNreXBozpaZxevZ1Ayc9KzNbq4XALxFpwcqboy2XlG5XINwU0bL0IWA2Xhs'
    b'orN+MMFa7dGuDZlLXr1p3uLuT82dO4veWf3jTarj5ZmQt/HQG1F2si8qiHeDCWL5fMV+N3K4'
    b'ta/f3n8WDBw3nt2dfx49RY5tCiYssQywfi2CHbd5tSSYoTIEDrQCHgOb5DiIGBO6Bjon4QxH'
    b'wenFFRZMMDzKdQRT4e/CrN4C1xXQWuKz2gytGaQltGIgvBGehfiqAHDF2mVZvVMDWnE7aYbW'
    b'BFK8LCGQ4gc/L2478SdvrBVkbTlEiqEVwJqgNa/8GPTi78f/r/MLrqNA0qW5v/YAAAAASUVO'
    b'RK5CYII=')

#----------------------------------------------------------------------
sold = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAA'
    b'7UlEQVQ4ja3SzypFURQG8J9LqZsSSSZMbklKykwZKnNvYGbIoxi6r2DoEQzMTJQTA1IUMsAA'
    b'+RODs26dbut0rz9frdZe3159fWvvxR8xGHkeq7jG628ENjCDRRR4/qmTkYjhEOsbAwm3g5Mu'
    b'7g33lbjFEwwlAgV20cR7cE1MRExjLUT2MoFPNKL5MbhRfOAGl1Ef1jk4RwsPFQcvXT1TIaaR'
    b'CBxjIeFTZAJ3mMRXhauel3HVKbIRYBbrNXcX2O/lbLNXQwfZHsASVtSv9YHyu9M3gCPl3GfK'
    b'xWlHPlVua9GPuzlsYSzqcWwH/3/4Bmr9LkZJQR6qAAAAAElFTkSuQmCC')

#----------------------------------------------------------------------
add_item = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'FUlEQVQ4je2QP0vDcBCGn/slFa3QScGpZFDbJuYDFMS5FAQ/gDrp4uAnagUX3dw7CULpHpEu'
    b'mcTJUSiYpM05tEhJ2lidvem4e5/3/kBBHLj1G9dtdIs0pqipyJnA+Z8NVol/A5BswfPql6Jy'
    b'MlEujPAKkCpVI3RRHl6Gw8683va8xi1KM4oTPwzDCORQoW0Mj+h0w1leA96BjuM465vljWeU'
    b'vo3SBPbKZbaBN8sqXaXjxFHl6HuMUkMYRHFyDVCp2FuTMbsImvtBEAQjY5faAk9zhw6iKGmF'
    b'YfiR1S98YhAEo884OQbpgfSWwQD2oiLADGgt6+cM0tSu+v7+2k/AVGt2cgaaSl+xVuGzG8g9'
    b'cPprEhC4+wIl/12P1Jx7ngAAAABJRU5ErkJggg==')

#----------------------------------------------------------------------
small_label = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAA'
    b'20lEQVQ4jaXRsUpCURzH8Y9lRFarBi6+Q6PQ0NAzWFCT0iy4qe09gw9gj9BDFA2Vg9EYFM1J'
    b'BGFD54Ze7vVe7buc8+d/vj/+fw7/pJDjzREOUMRuOO8wwPd6htxFD7f4wCtecI4pbooZ8gnq'
    b'eIv1ptiHtQz5MMglXOMy9DfwJewTp4fjGRm2wySbod7CZ1JAkgzvqGES6p2Z+5z8iErKWhF7'
    b'ePb7O3+cYZRTHqEfb1yhuaoMDYxRTZEri+SIdkpIGQ+4yJgwMaSM+7xyRAdPaMkxdhoNDHG6'
    b'irwUP5/6Lha/eHRrAAAAAElFTkSuQmCC')

move_bin = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'SElEQVQ4jaWSr04DQRCHv9nbGrheTZMagiDB8ACgICEBHIYEDB6DAYsnvAAWJAaFrsSVJ6gi'
    b'4JpcSLlSSsPuDuLaUgJ3acLPzb9vZ3ZGAGqrB2cq4ZCRRKX92rrdA2g0GvOdTqdPgSyAouvO'
    b'sKIoABVv5gCSJFnrDwbnwFYpoEhB9U7hOU6S5s9ACM7ao49u96kcILJr4OIty7an/XEcb1rn'
    b'ToETCyDIvQ26CEJuaxvgPcsegN1fbVv7+Ol9bTKCGHODpzVOEDSdyh+UdWnzWf2lGt2A/BcN'
    b'0gMWygp/AFAiH1Gd2sLLLMX5Y/9U3oHgo0CmYnxuhtLt/AKYyB/rp10eOwXS4pI/AOrsoZrv'
    b'U0alDezNDig45SI555YEuhPAX6rX69XhcLjvnGtGUXSFMTIJhuB9pXJUCkjTtAdcj8yd0hGK'
    b'TnkWfQEPoX6yAN/clAAAAABJRU5ErkJggg==')

#----------------------------------------------------------------------
return_back = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'N0lEQVQ4jc2QMUvDUBSFv5u8BoVS9R+42AqdRVwEpyK42lmHgjjoIA5Nly5VJ2cRHMSt4KSL'
    b'myJoZxHUIOrgKrgItklzHVpDqy1EQfDA48LhvO+8d+HfqWKnZytmPBc3b3VdTmRWRTi2VFNx'
    b'AQJQJus4drCD6GLL1ktEnr9EfVH1MBwU372HLsCGSR8BczFLG4gsu/7dXvQFtewiymNMgIPq'
    b'7pYZm44ApcbNNU1rAuQMQFTybuBJ50kEA0lgrQ2xQqxSBABwuX1JBs0cwn6v2nWu3tzA2xao'
    b'tRydAjCdoRXu6/gslBkd7vd+be/tU6ZXqMzT63cvm3RMYwmYbKMuIsCmnZlX0aqo5PtPv9pR'
    b'3gSpdO3gB6ojWnAD7xzABpgxIykRGQolPOk/GQQ5lMAquKF3+oviP9IHzZh25SBCeHYAAAAA'
    b'SUVORK5CYII=')

return_sold = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'l0lEQVQ4jZ2PzUtUYRTGf+e9c4eCCAJpI7QQxyCIcSBo00KwhYtmoZTWok0g4gitBMF/oV3Q'
    b'lUAQBle2zo3kRgKFrn2Qi7kqbkKYEAMFyRnve9x0436Nkc/ufc5zfud5hYv0ZMnpCw4WrKH7'
    b'xDjVfX/iJB2RUnnukYjWVWlIwakG/sRBNOwre3UVngEIrLntrqGtrdFWHGC2vzaXCbmHYV+t'
    b'nYxfV6Gp8Apk0cI6HF3r2La38uZxqd9bz/hlb6bU773ttCd/g/dfX5fTwk9gLRXZEOGXqg4l'
    b'FyUIvkxOFSJjZ+PlUW/F+yjKw0RQ1Ec5hqSvUAQwcdNY3nf8Y1qqKxmA6P8AbBbQ+FZrADvJ'
    b'Q1QVnqfWD7dv3/yUAfzpkW5xB3iQSMAH3o2GuQBrmQeOLyjfClXnYrCsbt31brguPXkz23J/'
    b'7H0fb0bvnC/AVZGKUWYLZ+Hh7mbN392s+VdOi3smZNp1WgPxbC7AGh1DGVHjDEZeu/i7gvBU'
    b'RV78E+AU7ayqjLntrnrkBZ+nVgWGQ8cZz9u5tM4BzDiPk5BwL7kAAAAASUVORK5CYII=')

discontinue = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAB'
    b'YElEQVQ4jZWTvU4CURCFv7kiCRK1wEgoDFE0klj6Di5raHkIjUKp0ZoH0NegMibsuu9AqRHF'
    b'Pxp/Io2ukGjYsQFFYpQ93Z3Md86Z4gpDOi0UoomXN1tRSwxzAKLSVMVrTcWdlUrlfXBfBh8P'
    b'a+t5jB4AC8PGPV0pWky5brU/MF9wLlfE6NEfMEBGkON7y9760aCXfDRo+I8CFfIpx3HktFCI'
    b'Jl79MyAzItzPvmlNxrNmxvfXw8MAOp/wfSsSBKyJwNjSEsRio7HtNt1GA1G1IiKkTXaZWLkc'
    b'Kr+zt0/3op42IBq+fk+KRgTugvM6nZ1dmJgYDeyfgDYjqngIm91GI3yBwLgm+fxYBcLTcN2a'
    b'jntGarUPRUtAEALuirCxUqm8G4CU61ZVGdUkUJVS0nE8GPpM97Zti3IILP6KCpeiup103ZPv'
    b'0ZB0dXX8cXY2J6qWiqR741vASz49uVKrfQzufwJq/Iuj0yotzgAAAABJRU5ErkJggg==')

excel_png = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwY'
    b'AAAA90lEQVR4nGNgGHTAsN5QSq/W0Fe31rBBt9Zws26t4TOiNOrWGh7WqzX8pFdr9B8d+6z3'
    b'X4WMvdcFLMIwQA+LRoQBARgYqwEBk4L/p8xPB2uKnZUA5oPYINBxqus/DOA0wK3H8//n75//'
    b'R86I+f/m89v/nn2+YANAmhN2JINpEMZpgF6t0f8Z+2f9f/fl3f+JuyfDvXDk6dH/xQfLwDQI'
    b'4zVg7qH5YNun75tJugEhU8LBtgdODv3/8dvH/34TA0nzQsT06P9RM2PBmuLnJP0PmhxKWiDq'
    b'URKNupQmJChg1Ko3VNGtMw7VrTVs06sx2qZXY/gcl+LBAQDC8iqAD8RGPAAAAABJRU5ErkJg'
    b'gg==')

barcode_png = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwY'
    b'AAAApklEQVR4nO2TSwrCQBBEH4ILN3oAkWTjRfyscgWF3MytkiMIBvViUkMNNEaICS4t6Onu'
    b'oaoWwxTAHngAV+BMPy7mSrPTxROYMxwLa2kZj1ZH42Xt2gAzoHLXTpgzL2oTatcJKO1eeifM'
    b'mddB/Tfgp29QADf3bFB8a7AEJsDKXTth7hg07kfg8Mn5DZGXtPkrT119iLykVSAUjKGQRolM'
    b'kRwT5zuwfQFrEjcuFE+3/wAAAABJRU5ErkJggg==')
