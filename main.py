# Import packages
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS          # https://amueller.github.io/word_cloud/references.html
import os

# Plot word cloud and save it
def plot_and_save_cloud(wordcloud, img_fname):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off")
    # Save it
    plt.savefig(img_fname)

# Read input file, one entry per line
def load_input_file(input_file, separator=','):
    entries = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        if not (line.startswith('#') or line.startswith(';') or line.startswith('!')) and len(line.strip()) > 0:
            entries.append(line.strip())
    return separator.join(entries)

if __name__ == '__main__':
    print('Starting...')

    # Define the name of the output file (image)
    img_save_name_tail = 'collaborator_banners.png'

    # Correct the output file name.
    img_save_name = os.path.join(os.path.abspath(os.getcwd()), 'example_data', img_save_name_tail)
    
    # Define the name of the input file (text)
    txt_input_tail = 'input_file.txt'

    # Correct the input file name.
    txt_input = os.path.join(os.path.abspath(os.getcwd()), 'example_data', txt_input_tail)

    # Load the contents of the input file
    names = load_input_file(txt_input)

    # In case you want to change the default splitting character
    regexp=None

    # Generate word cloud
    wordcloud = WordCloud(width = 3000, height = 2000, 
        background_color='salmon', colormap='Pastel1', collocations=True, 
        normalize_plurals = False, stopwords = STOPWORDS, regexp=regexp).generate(names)

    # Plot
    plot_and_save_cloud(wordcloud, img_save_name)

    print('Done.\n')

