import pandas as pd

def tableShow(ySetTest, yPredTest):
    header_data = {"Y (Actual)": ySetTest, "Y (Predicted)": yPredTest}
    df = pd.DataFrame(header_data)
    print("\n", df.to_string(index=False))